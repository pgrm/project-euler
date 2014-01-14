"""
not part of project-euler just a helper function to create prime numbers which are necessary for multiple solutions
"""

import math

def create_all_primes(condition_to_continue):
    primes = [2, 3]
    i = 3

    while condition_to_continue(primes, i):
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


def create_primes(highest_prime):
    return create_all_primes(lambda primes, i: i < highest_prime)


def create_n_primes(amount):
    return create_all_primes(lambda primes, i: len(primes) < amount)