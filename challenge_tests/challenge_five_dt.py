import unittest

from helpers.selenium_base import SeleniumBaseTest
from helpers.driver_manager import DriverManager
from selenium.webdriver.common.by import By
import helpers.url_helpers as url_helpers

"""
HW1:
https://www.doterra.com/US/en/using-essential-oils
There is a section on the homepage ( Here are the 10 most popular essential oils: ) that has a URL that goes to a dead page.
	
HW2:
Validate all the URLs in the footer
	
HW3:
https://www.doterra.com/US/en/product-education-blends 
Figure out how many of the products have the word doTERRA in it, how may are DigestZens and how many fit into a misc category. This is the same as challenge 5.
	
HW4:
Create a Driver Manager.
"""






class ChallengeFiveDT(SeleniumBaseTest):

    def setUp(self):
        super().setUp()


    def tearDown(self):
        super().tearDown()


    def test_hw1(self):
        self.go("https://www.doterra.com/US/en/using-essential-oils")
        self._check_urls(xpath_prefix="//div[@id='content_body']", url_prefix="https://www.doterra.com")

    def test_hw2(self):
        self.go("https://www.doterra.com/US/en/using-essential-oils")
        self._check_urls(xpath_prefix="//*[@id='footer']", url_prefix="https://www.doterra.com")

    def test_hw3(self):
        self.go("https://www.doterra.com/US/en/product-education-blends")

        oils_to_check = []
        oils = self.driver.find_elements_by_xpath('//div[@id="content"]//span[@class ="title"]')
        for oil in oils:
            oils_to_check.append(oil.text)

        self.doterra = 0
        self.digestzen = 0
        self.misc = 0

        self.total = len(oils_to_check)

        for oil_string in oils_to_check:
            if "doterra" in oil_string.lower():
                self.doterra = self.doterra + 1
            elif "digestzen" in oil_string.lower():
                self.digestzen = self.digestzen + 1
            else:
                self.misc = self.misc + 1

        print("doTERRA: ", self.doterra)
        print("DigeztZen", self.digestzen)
        print("MISC: ", self.misc)

        self.assertEqual(self.total, self.doterra + self.digestzen + self.misc)

    def test_hw4(self):
        driver=DriverManager().driver
        print(type(driver))
        self.assertIn("WebDriver", str(type(driver)))

    def _check_urls(self, xpath_prefix="", url_prefix="https"):
        xpath = xpath_prefix + "//a"
        print ("check_urls for " + xpath)
        urls = set()

        for elem in self.driver.find_elements_by_xpath(xpath):
            url = elem.get_attribute("href")
            print(url)

            if str(url).startswith(url_prefix):
                print("started with ", url_prefix)
                print("adding: ", url, "to the set")
                urls.add(str(url))

        print ("urls to check: ", urls)
        for urll in urls:
            #if "melaleuca" in urll:
            #    continue
            #url="https://www.doterra.com/US/en/p/melaleuca-oil"
            url = urll
            print(url)

            self.assertTrue(url_helpers.is_url_valid(url), "url returned bad return code")
            self.go(url)
            h123 = None

            try:
                #interrim solution to wait for the page to load before checking for "cannot be loaded"
                #(every doterra page has one of these.)
                h123 = self.get_present("//h1|//h2|//h3")
            except Exception as e:
                print("warn: " + str(e))
            print("h123 = ", h123)
            self.assertTrue(h123, "this does not appear to be a doterra page")

            cannot = None
            text = None
            try:
                cannot = self.get_present("//*[contains(@class,'page-notFound')]", timeout=1)
                #cannot = self.get_present('//h1[contains(text(),"cannot be found"]', timeout=10)
                text = cannot.text
            except Exception as e:
                print(str(type(e)))
                pass

            self.assertFalse(cannot, "\n\"Page Not found\" found for " + url)

            self.driver.back()


if __name__ == '__main__':
    unittest.main()