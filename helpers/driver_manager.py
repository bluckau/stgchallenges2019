from helpers.selenium_helpers import *


class DriverManager():
    def __init__(self, path=None):
        self.path = path
        self._driver = None

    @property
    def driver(self):
        print('Getting driver')
        path = self.path



        if self._driver:
            return self._driver

        print(path)
        if path:
            self._driver = webdriver.Chrome(path)
        else:
            self._driver = webdriver.Chrome()
        return self._driver

    @driver.setter
    def driver(self, driver):
        print('Setting driver to ' + driver)
        self._driver = driver

    @driver.deleter
    def driver(self):
        print('Deleting driver')
        del self._driver