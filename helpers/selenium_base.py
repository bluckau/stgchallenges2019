from helpers.driver_manager import *
from page_objects.copart import *

class SeleniumBaseTest(unittest.TestCase, SeleniumHelper):
    def setUp(self):
        self.driver_manager=DriverManager(R"c:\dev\webdrivers\chromedriver.exe")
        self.driver = self.driver_manager.driver


        self.copart = Copart(self.driver)

    def tearDown(self):
        if self.driver:
            self.driver.close()


