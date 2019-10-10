from challenge_tests.basetest import BaseTest
from helpers.selenium_helpers import *

"""
Challenge 2 - Asserts:
Many times, the general thought for an automation script is to go from point A to point B.  However, this doesn’t
measure if the test actually passed or not.  There are times when a button click doesn’t work or the action handler
going to a wrong page like a 404 page.  Just because the script worked and you are on a new page does not mean the test
passed.  That is where asserts come in.  In terminology, you can so soft or hard asserts.  Soft asserts checks the data
but does not stop the script from running.  Hard asserts will stop the script when it fails.  Soft asserts allows you to
build long running automation scripts like one what might span across 5 different pages.  When you write a script for
shopping for a product, you would typically to go the login page, product page, cart page, checkout summary page,
checkout verification page.  Rather than writing one script for each of these pages, you can build one test and add in
soft asserts and trigger warnings or print out to log files when there is failed scenario in the soft assertion.  Then
once you get to the final page, or final step, you can do a hard assertion to check for something like an order number.  

For this challenge, look through the different ways to do assertions.  Then write a script that will go to copart.com,
search for exotics and verify porsche is in the list of cars.  Use the hard assertion for this challenge.  

https://pythontips.com/2013/08/07/the-self-variable-in-python-explained/
https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
https://selenium-python.readthedocs.io/getting-started.html
https://www.tutorialspoint.com/python/assertions_in_python.htm
http://www.mahsumakbas.net/selenium-assertion-with-python-unittest/

Another tutorial on how to use webdriver’s getAttributes.  Example is in java but works the same in python.  
https://www.seleniumeasy.com/selenium-tutorials/how-to-get-attribute-values-using-webdriver

This example is an older video that explains verify vs assert.  The exact code is not relevant to our training but it’s
a good concept video to watch.  

https://www.youtube.com/watch?v=iw_NDJsLYt8

"""

class ChallengeTwo(BaseTest):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown

    def test_challenge_two(self):

        self.copart.search_item("Exotics")

        make = "Porsche"
        check = self.copart.is_make_listed(make)
        self.assertTrue(check, "{} was not in the list.".format(make))


if __name__ == '__main__':
    unittest.main()