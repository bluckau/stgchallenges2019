import unittest
#from selenium.webdriver.remote.webdriver import *

from selenium import webdriver

class ChallengeOne(unittest.TestCase):

    def setUp(self):
        self.driver = self.driver = webdriver.Chrome(R"c:\dev\webdrivers\chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge_one(self):
        self.driver.get("https://www.google.com/")
        self.assertIn("Google", self.driver.title)


if __name__ == '__main__':
    unittest.main()