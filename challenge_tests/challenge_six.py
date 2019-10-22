import unittest
from challenge_tests.copart_base_test import *

"""
Challenge 6 - Error Handling
Using a try/catch block can help you catch certain errors that might exist that you weren’t anticipating.  It can also
give you some type of behavior you want to take when something happens.  

Let’s say you are running a test script and the 4th step fails.  At this point, you can decide what you want it to do.
Do you want to try something else, or take a screenshot, or reset your browser of where you are at for the next step in
the script?  

Taking a screenshot is a common way to use the try catch block.  For this challenge, go to copart site, search for
nissan, and then for the model, search for “skyline”.  This is a rare car that might or might not be in the list for
models.  When the link does not exist to click on, your script will throw an exception.  Catch the exception and take a
screenshot of the page of what it looks like.  

"""

class ChallengeSix(CopartBaseTest):

    def setUp(self):
        super().setUp()


    def tearDown(self):
        super().tearDown()


    def test_challenge_six(self):
        """For this challenge, go to copart site"""
        make="Nissan"
        #model="skyline"
        copart = self.copart

        copart.search_item(make)

        model="versa"
        copart.filter_model(model)
        self.assertTrue(copart.check_for_model(model))


if __name__ == '__main__':
    unittest.main()