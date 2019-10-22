from helpers.selenium_base import SeleniumBaseTest
from page_objects.copart import *

class CopartBaseTest(SeleniumBaseTest):
    def setUp(self):
        super().setUp()
        self.copart = Copart(self.driver)
        self.driver.get("https://copart.com")
        self.driver.maximize_window()


    def tearDown(self):
        super().tearDown()

