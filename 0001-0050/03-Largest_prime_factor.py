"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
import primes

highestNumber = 600851475143
highestPrime = int(math.sqrt(highestNumber))
relevantPrimes = reversed(primes.create_primes(highestPrime))

for p in relevantPrimes:
    if highestNumber % p == 0:
        print str(p)
        break
