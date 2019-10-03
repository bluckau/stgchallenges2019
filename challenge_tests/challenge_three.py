import unittest
from selenium import webdriver

class ChallengeThree(unittest.TestCase):

    def setUp(self):
        self.driver = self.driver = webdriver.Chrome(R"c:\dev\webdrivers\chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge_three(self):
        driver = self.driver
        self.driver.get("https://copart.com")

        popular_makes = '//a[contains(@href, "popular/model") or contains(@href, "popular/make")]'
        elems = driver.find_elements_by_xpath(popular_makes)
        for make in elems:
            print("{} {}{}".format(make.text, "https://copart.com/", make.get_attribute("href")))


if __name__ == '__main__':
    unittest.main()