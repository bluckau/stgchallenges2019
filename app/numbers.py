from app.strings import Strings

class Fib:

    @classmethod
    def fibonacci_translated(cls, n):
        return Strings.convert_number_to_words(cls.fibonacci(n))

    @classmethod
    def fibonacci(cls, n):
        array = [0]

        if n == 0:
            return 0

        for i in range(1, n + 1):
            if i == 1:
                array.append(1)
            else:
                array.append(array[i - 1] + array[i - 2])

        return array[n]


