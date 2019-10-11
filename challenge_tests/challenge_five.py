import unittest
from challenge_tests.copart_base_test import *

"""
Challenge 5 - If/Else/Switch
Decision making is what will make your automation run w/ some AI helping it.  Rather than building a script w/ hard 
coded variables, why not use if/else/switch to do some basic decision making.  Let’s say, for a shopping scenario, I
want to use Visa payment.  Then if I want to test MasterCard, should I write two sets of scripts?  Or should I write one
script that depending on the data/card I want to use, the script will use if/else/switch to select the appropriate 
payment method for me.  This way, I will only have one script to maintain but I can write as many tests as I want that
passes in a different set of data/variables that can be tested.  If someone changes the payment form, I would only have
to update one set of code instead of multiple sets of code.  This will help you make your automation more maintainable.
Another use in the decision making is to count bits of data.  

For this challenge, go to https://www.copart.com and do a search for “porsche” and change the  drop down for 
“Show Entries” to 100 from 20.  Count how many different models of porsche is in the results on the first page and
 return in the terminal how many of each type exists.  

Possible values can be “CAYENNE S”, “BOXSTER S”, etc.  

For the 2nd part of this challenge, create a switch statement to count the types of damages.
Here’s the types:
REAR END
FRONT END
MINOR DENT/SCRATCHES
UNDERCARRIAGE
And any other types can be grouped into one of MISC.  

https://www.w3schools.com/python/python_conditions.asp
"""

class ChallengeFive(CopartBaseTest):

    def setUp(self):
        super().setUp()


    def tearDown(self):
        super().tearDown()


    def test_challenge_five(self):
        copart = self.copart

        self.copart.search_item("Porsche")
        self.copart.select_per_page(100)


        models = self.copart.get_models_list()
        qty = len(models) #don't want to iterate over this list because we get stale element handles

        self.assertEqual(qty, 100, "There should be 100 rows!")

        models_dict = self.copart.get_models_dict(qty)
        #limit to 10 while troubleshooting
        i=0
        for k in models_dict.keys():
            if i < 10:
                print("{}: {}".format(k, models_dict.get(k)))

        #PART 2
        self.front = 0
        self.rear = 0
        self.minor = 0
        self.undercarriage = 0
        self.misc = 0

        damages_list = self.copart.get_damages_list()
        qty = len(damages_list)


        for i in range(qty):
            text = copart.get_damage_for_row(i+1)

            # No switch statement in Python so the definition of "the best way" is fuzzy. This was the best way given
            # this scenario and given we were to try to simulate the switch statement.

            if text == "REAR END":
                self.rear += 1
            elif text == "FRONT END":
                self.front += 1
            elif text == "MINOR DENT/SCRATCHES":
                self.minor += 1
            elif text == "UNDERCARRIAGE":
                self.undercarriage += 1
            else:
                self.misc += 1

        print("REAR END: ", self.rear)
        print("FRONT END: ", self.front)
        print("MINOR DENT/SCRATCHES: ", self.minor)
        print("UNDERCARRIAGE: ", self.undercarriage)
        print("MISC: ", self.misc)


if __name__ == '__main__':
    unittest.main()