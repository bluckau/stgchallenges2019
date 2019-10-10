import sys
import unittest
from app.numbers import Fib
from app.strings import Strings

"""
Challenge 4 - Operators and Functions:
For this challenge, we will be using operators and functions to tinker around w/ string concatenation and tokenization.  
String concatenation is the process of putting together a message using multiple variables.  The application of this can 
be for logging or capturing variables or using a dynamic variable that is found on a page before it’s used to trigger an 
action.  Tokenization is needed for breaking up a sentence or to break up a long string into arrays so that you can example 
each word.  It can also be used to pull variables out of the URLs.  There are endless uses.  

For this challenge, we are going to write a function that display the fibonacci sequence up to a certain number.  If I 
want the fibonacci for the 9 order of the sequence, I should see 21.  Keep your function to calculate the fibonacci 
sequence separate from the file that has the unittest.main().

However, to add additional challenge to this challenge, instead of displaying the number 21, I want the string 
representation of twenty one.  This will require you to use string concatenation to print out the string.  

https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/
https://www.programiz.com/python-programming/examples/fibonacci-recursion
https://www.youtube.com/watch?v=POQIIKb1BZA

Your console output will look something like this.

13 - thirteen
144 - one hundred forty four
7408 - seven thousand four hundred eight


Now that you know how to write a function, copy your previous challenge folder and create a new folder.  Now let’s refactor your “before” method and make it a one line call out to another function.  The reason why we do this is so that we only have one function that does our initialization of the driver.  Otherwise, the poor implementation would be to copy multiple lines from script to script.  When it comes time to change the “before” method, you will have to change it in multiple places versus one.  

**** Do not use someone else’s library.  You should write your own logic.  Keep non related classes separate.  ie. Fibnacci class has no relations to convertNumbertoString class ****
"""

class ChallengeFour(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fibonacci(self):
        self.assertEqual(Fib.fibonacci(0), 0)
        self.assertEqual(Fib.fibonacci(1), 1)
        self.assertEqual(Fib.fibonacci(2), 1)
        self.assertEqual(Fib.fibonacci(8), 21)  # zero based index so 8 is the 9th element in the sequence

    def test_convert_to_words(self):
        self.assertEqual(Strings.convert_number_to_words(2), "Two")
        self.assertEqual(Strings.convert_number_to_words(20), "Twenty")
        self.assertEqual(Strings.convert_number_to_words(21), "Twenty-One")
        self.assertEqual(Strings.convert_number_to_words(121), "One Hundred Twenty-One")
        self.assertEqual(Strings.convert_number_to_words(1121), "One Thousand One Hundred Twenty-One")
        self.assertEqual(Strings.convert_number_to_words(1000000), "One Million")
        self.assertEqual(Strings.convert_number_to_words(123123123),
                         "One Hundred Twenty-Three Million One Hundred Twenty-Three Thousand One Hundred Twenty-Three")

    def test_challenge_four(self):
        self.assertEqual(Fib.fibonacci_translated(1), "One")
        self.assertEqual(Fib.fibonacci_translated(2), "One")
        self.assertEqual(Fib.fibonacci_translated(3), "Two")
        self.assertEqual(Fib.fibonacci_translated(4), "Three")
        self.assertEqual(Fib.fibonacci_translated(6), "Eight")
        self.assertEqual(Fib.fibonacci_translated(99), "Two Hundred Eighteen Quintrillion Nine Hundred Twenty-Two Quadrillion Nine Hundred Ninety-Five Trillion Eight Hundred Thirty-Four Billion Five Hundred Fifty-Five Million One Hundred Sixty-Nine Thousand Twenty-Six")


if __name__ == '__main__':
    unittest.main()
