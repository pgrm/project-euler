"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

largest3DigitNumber = 999
largestPossibleProduct = 999 * 999


def is_palindrome(number):
    str_number = str(number)
    reverse_str_number = str_number[::-1]

    if str_number == reverse_str_number:
        return True
    else:
        return False


def is_product(number):
    divisor = largest3DigitNumber

    while True:
        if number % divisor == 0:
            return True
        if number / divisor > divisor:
            return False
        divisor -= 1


while True:
    if is_palindrome(largestPossibleProduct):
        if is_product(largestPossibleProduct):
            break
    largestPossibleProduct -= 1

print str(largestPossibleProduct)