import unittest
#from selenium.webdriver.remote.webdriver import *
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChallengeTwo(unittest.TestCase):

    def setUp(self):
        self.driver = self.driver = webdriver.Chrome(R"c:\dev\webdrivers\chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge_two(self):
        driver = self.driver
        self.driver.get("https://copart.com")

        search_id = "input-search"
        elem = driver.find_element_by_id(search_id)
        make="Porsche"
        elem.send_keys(make)

        button = "//button[contains(text(), 'Search')]"
        elem = driver.find_element_by_xpath(button)
        elem.click()

        make_lower=make.lower()
        make_upper=make.upper()

        xpath = "//span[@data-uname='lotsearchLotmake' and translate(text(),'{}','{}') = '{}']".format(make_upper, make_lower, make_lower)
        print("xpath: " + str(xpath))

        elem = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

        self.assertTrue(elem, "{} was not in the list.".format(make))


if __name__ == '__main__':
    unittest.main()