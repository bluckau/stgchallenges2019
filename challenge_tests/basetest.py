from helpers.selenium_helpers import *
from page_objects.copart import *

class BaseTest(unittest.TestCase, SeleniumHelper):
    def setUp(self):
        self.driver = webdriver.Chrome(R"c:\dev\webdrivers\chromedriver.exe")
        self.driver.get("https://copart.com")
        self.driver.maximize_window()

        self.copart = Copart(self.driver)

    def tearDown(self):
        if self.driver:
            self.driver.close()
