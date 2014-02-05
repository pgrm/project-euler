"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from math import sqrt

import primes
import permutations

primesToCheck = primes.create_primes(sqrt(987654321))
primeFound = False


def is_prime(number):
    limit = sqrt(number)
    for p in primesToCheck:
        if p > limit:
            return True
        elif number % p == 0:
            return False

    return True


for x in xrange(10, 1, -1):
    allPermutations = permutations.permutations(range(1, x))

    for perm in sorted([permutations.combine_numbers(y) for y in allPermutations], reverse=True):
        if is_prime(perm):
            print str(perm)
            primeFound = True
            break

    if primeFound:
        break
