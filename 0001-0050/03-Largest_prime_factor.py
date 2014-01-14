"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math


def create_primes(highest_prime):
    primes = [3]  # 2 is also a prime but since the number in question isn't dividable by 2 anyway, just skip it
    i = 3

    while i < highest_prime:
        i += 2
        si = math.sqrt(i)
        is_prime = True

        for p in primes:
            if i % p == 0:
                is_prime = False
            if p > si:  # no use to check above the sqrt of i
                break

        if is_prime:
            primes += [i]

    return primes


highestNumber = 600851475143
highestPrime = int(math.sqrt(highestNumber))
relevantPrimes = reversed(create_primes(highestPrime))

for p in relevantPrimes:
    if highestNumber % p == 0:
        print str(p)
        break
