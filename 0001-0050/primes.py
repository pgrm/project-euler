"""
not part of project-euler just a helper function to create prime numbers which are necessary for multiple solutions
"""

import math

tmp_primes = [2, 3]


def create_all_primes(condition_to_continue, primes=[2, 3]):
    i = primes[-1]

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


def is_number_prime(number):
    global tmp_primes

    if number < 2:
        return False

    highest_prime = tmp_primes[-1]
    if highest_prime*highest_prime < number:
        tmp_primes = create_all_primes((lambda primes, i: primes[-1]*primes[-1] <= number), tmp_primes)

    for p in tmp_primes:
        if number % p == 0:
            return False
        if p*p > number:
            return True