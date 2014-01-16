"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

def digit_to_string(digit):
    digit = int(digit)

    return {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }[digit]


def number_to_string(number):
    if number >= 1000:
        return digit_to_string(number / 1000) + 'thousand' + number_to_string(number - 1000)
    elif number >= 100:
        string = digit_to_string(number / 100) + 'hundred'
        if number % 100 > 0:
            return string + 'and' + number_to_string(number % 100)
        else:
            return string
    elif number >= 20:
        string = {
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety'
        }[int(number / 10) * 10]

        if number % 10 > 0:
            return string + number_to_string(number % 10)
        else:
            return string
    elif number >= 10:
        return {
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen'
        }[number]
    else:
        return digit_to_string(number)


numberOfLetters = 0
for i in xrange(1, 1001):
    numberOfLetters += len(number_to_string(i))

print str(numberOfLetters)