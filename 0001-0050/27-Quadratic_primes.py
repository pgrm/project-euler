"""
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^1 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces
the maximum number of primes for consecutive values of n, starting with n = 0.
"""

import primes


def solve_formula(a, b, n):
    return n*n + a*n + b


def get_number_of_consecutive_primes(a, b):
    n = 0
    while primes.is_number_prime(solve_formula(a, b, n)):
        n += 1

    return n

product = 0
numberOfConsecutivePrimes = 0

for A in xrange(-999, 1000):
    for B in xrange(-999, 1000):
        newNumberOfConsecutivePrimes = get_number_of_consecutive_primes(A, B)
        if newNumberOfConsecutivePrimes > numberOfConsecutivePrimes:
            numberOfConsecutivePrimes = newNumberOfConsecutivePrimes
            product = A * B

print product