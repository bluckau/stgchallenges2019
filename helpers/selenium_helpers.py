import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
TIMEOUT = 120

class SeleniumHelper():

    def __init__(self):

        if not self.driver:
            self.driver = webdriver.Chrome(R"c:\dev\webdrivers\chromedriver.exe")

    def wait_xpath(self, xpath:str, timeout:int=TIMEOUT):
        #print("wait_xpath: {} with timeout {}".format(xpath, timeout))
        elem = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return elem


    def wait_id(self, id:str, timeout:int=TIMEOUT):
        #print("wait_id: {} with timeout {}".format(id, timeout))
        elem = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, id))
        )
        return elem

    def go_to(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_text_from_string_located_by_xpath(self, xpath):
        for i in range(5):
            try:
                e = self.wait_xpath(xpath)
                text = e.text.strip()
                return text
            except StaleElementReferenceException as e:
                if i > 5:
                    raise StaleElementReferenceException from e
                else:
                    print("Caught stale element handle")
                    time.sleep(1)

