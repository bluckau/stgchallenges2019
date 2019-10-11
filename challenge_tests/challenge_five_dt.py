import unittest

from helpers.selenium_base import SeleniumBaseTest
from helpers.driver_manager import DriverManager
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
        pass

    def test_hw2(self):
        pass

    def test_hw3(self):
        pass

    def test_hw4(self):
        driver=DriverManager().driver
        print(type(driver))
        self.assertIn("WebDriver", str(type(driver)))


if __name__ == '__main__':
    unittest.main()