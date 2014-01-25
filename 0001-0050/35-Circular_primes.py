"""
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from collections import deque
import primes
import permutations

allPrimes = primes.create_primes(1000*1000)
countOfCircularPrimes = 0

for prime in allPrimes:
    isCircularPrime = True
    digits = deque(permutations.split_into_digits(prime))

    for i in xrange(0, len(digits)):
        digits.rotate(1)
        newPrime = permutations.combine_numbers(digits)

        if newPrime not in allPrimes:
            isCircularPrime = False
            break

    if isCircularPrime:
        countOfCircularPrimes += 1

print str(countOfCircularPrimes)