"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

number = 1

for i in xrange(0, 1000):
    number <<= 1

digitsSum = sum([int(c) for c in str(number)])

print digitsSum