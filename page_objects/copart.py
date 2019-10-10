import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from helpers.selenium_helpers import SeleniumHelper

TIMEOUT = 120


class Copart(SeleniumHelper):
    def __init__(self, driver):
        self.driver = driver

    def search_item(self, item):

        search_id = "input-search"
        elem = self.wait_id(search_id)
        elem.send_keys(item)

        button = "//button[contains(text(), 'Search')]"
        elem = self.wait_xpath(button)
        elem.click()


    def select_per_page(self, num):
        select_xpath = '//label[contains(text(),"Show")]/select'
        select_elem = self.wait_xpath(select_xpath)
        select = Select(select_elem)
        select.select_by_value(str(num))

    def get_models_list(self):
        models_xpath = "//*[@id='serverSideDataTable']/tbody/tr/td[6]/span"
        self.wait_xpath(models_xpath)
        elems = self.driver.find_elements_by_xpath(models_xpath)
        return elems

    def get_models_dict(self, qty):
        models_dict = {}
        for i in range(qty):
            model_xpath = "//*[@id='serverSideDataTable']/tbody/tr[{}]/td[6]/span".format(i+1)
            e = self.wait_xpath(model_xpath)
            text = self.get_text_from_string_located_by_xpath(model_xpath)
            if text in models_dict.keys():
                num = models_dict.get(text)
            else:
                num = 0
            models_dict.update({text: int(num) + 1})
        return models_dict

    def get_damages_list(self):
        damages_xpath = "//*[@id='serverSideDataTable']/tbody/tr/td[12]/span"
        self.wait_xpath(damages_xpath)
        elems = self.driver.find_elements_by_xpath(damages_xpath)
        qty = len(elems)
        print("found: {} elems".format(qty))
        return elems

    def get_damage_for_row(self, row):
        damage_xpath = "//*[@id='serverSideDataTable']/tbody/tr[{}]/td[12]/span".format(row)
        e = self.wait_xpath(damage_xpath)
        return e.text

    def is_make_listed(self, make):
        make_lower=make.lower()
        make_upper=make.upper()

        xpath = "//span[@data-uname='lotsearchLotmake' and translate(text(),'{}','{}') = '{}']".format(make_upper, make_lower, make_lower)
        print("xpath: " + str(xpath))

        elem = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        if elem:
            return True
        else:
            return False


    def get_popular_makes(self):
        xpath = '//a[contains(@href, "popular/model") or contains(@href, "popular/make")]'
        elems = self.driver.find_elements_by_xpath(xpath)
        return elems