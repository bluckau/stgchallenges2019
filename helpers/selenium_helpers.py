import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
TIMEOUT = 10

class SeleniumHelper():

    def __init__(self):

        if not self.driver:
            self.driver = webdriver.Chrome(R"c:\dev\webdrivers\chromedriver.exe")

    def get(self, item, loc_str, timeout=TIMEOUT):
        self.get_clickable(item, loc_str, timeout)

    def get_clickable(self, item:str, loc_str:str = None, timeout:int=TIMEOUT):
        print("wait_clickable: {} with timeout {}".format(loc_str, timeout))

        locator = self.resolve(item, loc_str)
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def get_visible(self, item:str, loc_str:str = None, timeout:int=TIMEOUT):
        print("wait_visible_id: {} with timeout {}".format(id, timeout))

        locator = self.resolve(item, loc_str )
        if isinstance(locator, WebElement):
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of(locator)
            )

        else:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )


    def get_present(self, item:str, loc_str:str = None, timeout:int=TIMEOUT):
        if isinstance(item, WebElement):
            return item

        locator = self.resolve(item, loc_str)

        print("Locator: " + str(locator))
        print("wait_present: {} with timeout {}".format(locator, timeout))
        elem = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return elem


    def go(self, url):
        self.driver.get(url)

    def title(self):
        return self.driver.title

    def send(self, item, loc_str=None, text=None):
        if not text:
            raise InvalidArgumentException("text must be an object")
        elem = self.get_clickable(item, loc_str)
        elem.send_keys(str(text))
        return elem

    def text(self, item, loc_str = None):
        elem = self.get_visible(item, loc_str)
        text = elem.text
        return text.strip()

    def hit(self, item, loc_str=None):
        elem = self.get_clickable(item, loc_str)
        elem.click()
        return elem

    def resolve(self, item=None, loc_str=None):
        if isinstance(item, WebElement):
            setattr(item, "loc_str", loc_str)
            return item

        if item in [By.XPATH, By.ID, By.CLASS_NAME, By.CSS_SELECTOR, By.LINK_TEXT, By.NAME, By.PARTIAL_LINK_TEXT, By.TAG_NAME]:
            by = item
            return (by, loc_str)

        elif loc_str and loc_str.startswith("//"):
            return (By.XPATH, loc_str)

        elif item and item.startswith("//"):
            return (By.XPATH, item)
        else:
            if loc_str:
                return (By.ID, loc_str)
            else:
                return (By.ID, item)




