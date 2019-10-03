class Fib:

    @classmethod
    def fibonacci_translated(cls, n):
        return Numbers.convert_to_words(cls.fibonacci(n))

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

class Numbers:
    def convert_to_words(num: int):
        digits_and_teens = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
                            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["No", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        divs = ["No", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintrillion", "Sextillion",
                "Septillion", "Octillion", "Nonillion", "Decillion"]

        if(num == 0):
            print(digits_and_teens[0])

        def print_three_digits(i):
            # make sure only the last 3 digits:
            i = i % 1000

            hundreds_digit = i // 100
            out_string = print_two_digits(i % 100)

            if hundreds_digit > 0:
                out_string = " Hundred ".join([digits_and_teens[hundreds_digit], out_string])

            return out_string

        def print_two_digits(i):
            # make sure only the last 2 digits
            i = i % 100

            last_digit = i % 10

            if i < 1:
                return ""
            if i < 20:
                return digits_and_teens[i]
            else:
                return "{}{}".format(tens[i // 10], "-" + digits_and_teens[last_digit] if last_digit else "")

        # initial string with the first three digits from the right
        str_from_right = print_three_digits(num)

        # get the thousands, millions, etc. and append to the left

        iter = 0
        while (num > 999):
            iter += 1
            num = num // 1000
            last = print_three_digits(num)
            list = [last, divs[iter]]
            if str_from_right:
                list.append(str_from_right)

            if last:
                str_from_right = " ".join(list)

        return str_from_right


