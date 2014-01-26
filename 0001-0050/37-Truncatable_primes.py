"""
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import primes

allPrimes = primes.create_primes(1000*1000)


def is_left_truncatable(prime):
    for i in xrange(1, len(str(prime))):
        if (prime % (10 ** i)) not in allPrimes:
            return False
    return True


def is_right_truncatable(prime):
    for i in xrange(1, len(str(prime))):
        if (prime / (10 ** i)) not in allPrimes:
            return False
    return True


sumOfTruncatablePrimes = 0

for p in allPrimes:
    if p < 10:
        continue

    if is_left_truncatable(p) and is_right_truncatable(p):
        sumOfTruncatablePrimes += p

print str(sumOfTruncatablePrimes)
