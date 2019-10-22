from challenge_tests.copart_base_test import *
import unittest

"""
Challenge 3 - Loops:
Loops can be used to write your own wait statements.  They can also be used to iteration through a list of items.  

For this challenge, go to copart and print a list of all the “Popular Items” of vehicle Make/Models on the home page and
the URL/href for each type.  This list can dynamically change depending on what is authored by the content creator but 
using a loop will make sure that everything will be displayed regardless of the list size.

https://www.pythonforbeginners.com/loops/for-while-and-nested-loops-in-python
https://www.learnpython.org/en/Loops
https://www.w3schools.com/python/python_for_loops.asp
https://devhints.io/xpath
https://www.w3schools.com/xml/xpath_intro.asp
https://www.red-gate.com/simple-talk/dotnet/.net-framework/xpath,-css,-dom-and-selenium-the-rosetta-stone/

Your output in the console would look like:
IMPREZA - https://www.copart.com/popular/model/impreza
CAMRY - https://www.copart.com/popular/model/camry
ELANTRA - https://www.copart.com/popular/model/elantra
SONATA - https://www.copart.com/popular/model/sonata
COROLLA - https://www.copart.com/popular/model/corolla
ALTIMA - https://www.copart.com/popular/model/altima
FORESTER - https://www.copart.com/popular/model/forester
OPTIMA - https://www.copart.com/popular/model/optima
IMPALA - https://www.copart.com/popular/model/impala
PRIUS - https://www.copart.com/popular/model/prius
FORD - https://www.copart.com/popular/make/ford
TOYOTA - https://www.copart.com/popular/make/toyota
CHEVROLET - https://www.copart.com/popular/make/chevrolet
DODGE - https://www.copart.com/popular/make/dodge
HONDA - https://www.copart.com/popular/make/honda
NISSAN - https://www.copart.com/popular/make/nissan
SUBARU - https://www.copart.com/popular/make/subaru
"""

class ChallengeThree(CopartBaseTest):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_challenge_three(self):
        elems = self.copart.get_popular_makes()

        for make in elems:
            print("{} {}{}".format(make.text, "https://copart.com/", make.get_attribute("href")))


if __name__ == '__main__':
    unittest.main()