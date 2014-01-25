"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import permutations

fact = {}

for x in xrange(0, 10):
    f = 1
    for y in xrange(2, x + 1):
        f *= y

    fact[x] = f

factSum = 0

for i in xrange(10, 1000*100):  # found out experimentally
    if i == sum([fact[j] for j in permutations.split_into_digits(i)]):
        factSum += i

print str(factSum)