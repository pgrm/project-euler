"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import primes

primeNumbers = primes.create_primes(20)
primeFactors = {}


def get_prime_factors(number):
    prime_factors = {}
    original_number = number

    for p in primeNumbers:
        number = original_number
        factor = 0

        while number % p == 0:
            number /= p
            factor += 1

        prime_factors[p] = factor

    return prime_factors


def merge_prime_factors(new_prime_factors):
    for p in new_prime_factors:
        if p not in primeFactors:
            primeFactors[p] = new_prime_factors[p]
        else:
            primeFactors[p] = max(primeFactors[p], new_prime_factors[p])


for i in xrange(2, 20):
    merge_prime_factors(get_prime_factors(i))

product = 1
for x in primeFactors:
    while primeFactors[x] > 0:
        product *= x
        primeFactors[x] -= 1

print str(product)