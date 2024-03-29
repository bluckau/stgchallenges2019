from helpers.selenium_helpers import *
from helpers.selenium_base import *

class ChallengeOne(SeleniumBaseTest, SeleniumHelper):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_challenge_one(self):
        self.go("https://www.google.com/")
        self.assertIn("Google", self.title())


if __name__ == '__main__':
    unittest.main()