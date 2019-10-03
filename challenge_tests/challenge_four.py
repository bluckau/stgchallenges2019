import sys
import unittest
from app.numbers import *


class ChallengeFour(unittest.TestCase):
    def setUp(self):
        self.prepare()

    def tearDown(self):
        self.clean_up()

    def test_fibonacci(self):
        self.assertEqual(Fib.fibonacci(0), 0)
        self.assertEqual(Fib.fibonacci(1), 1)
        self.assertEqual(Fib.fibonacci(2), 1)
        self.assertEqual(Fib.fibonacci(8), 21)  # zero based index so 8 is the 9th element in the sequence

    def test_convert_to_words(self):
        self.assertEqual(Numbers.convert_to_words(2), "Two")
        self.assertEqual(Numbers.convert_to_words(20), "Twenty")
        self.assertEqual(Numbers.convert_to_words(21), "Twenty-One")
        self.assertEqual(Numbers.convert_to_words(121), "One Hundred Twenty-One")
        self.assertEqual(Numbers.convert_to_words(1121), "One Thousand One Hundred Twenty-One")
        self.assertEqual(Numbers.convert_to_words(1000000), "One Million")
        self.assertEqual(Numbers.convert_to_words(123123123),
                         "One Hundred Twenty-Three Million One Hundred Twenty-Three Thousand One Hundred Twenty-Three")

    def test_challenge_four(self):
        self.assertEqual(Fib.fibonacci_translated(1), "One")
        self.assertEqual(Fib.fibonacci_translated(2), "One")
        self.assertEqual(Fib.fibonacci_translated(3), "Two")
        self.assertEqual(Fib.fibonacci_translated(4), "Three")
        self.assertEqual(Fib.fibonacci_translated(6), "Eight")
        self.assertEqual(Fib.fibonacci_translated(99), "Two Hundred Eighteen Quintrillion Nine Hundred Twenty-Two Quadrillion Nine Hundred Ninety-Five Trillion Eight Hundred Thirty-Four Billion Five Hundred Fifty-Five Million One Hundred Sixty-Nine Thousand Twenty-Six")

    def prepare(self):
        print("nothing really to do to prepare right now")

    def clean_up(self):
        print("nothing really to break down")

if __name__ == '__main__':
    unittest.main()
