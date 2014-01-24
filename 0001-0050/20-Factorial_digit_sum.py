"""
n! means n x (n - 1) x ... x 3 x 3 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

bigNumber = 1
bigNumberSum = 0

for i in xrange (1, 101):
    bigNumber *= i

while bigNumber > 0:
    bigNumberSum += bigNumber % 10
    bigNumber /= 10

print str(bigNumberSum)