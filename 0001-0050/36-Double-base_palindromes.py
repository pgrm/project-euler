"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def is_palindrome(text):
    reverse_text = text[::-1]
    return text == reverse_text


sumOfPalindromes = 0

for i in xrange(0, 1000*1000):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        sumOfPalindromes += i

print str(sumOfPalindromes)