from challenge_tests.basetest import BaseTest
from helpers.selenium_helpers import *


class ChallengeOne(unittest.TestCase, SeleniumHelper):

    def setUp(self):
        self.driver = webdriver.Chrome(R"c:\dev\webdrivers\chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge_one(self):
        self.go_to("https://www.google.com/")
        self.assertIn("Google", self.get_title())


if __name__ == '__main__':
    unittest.main()