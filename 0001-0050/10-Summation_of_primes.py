"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import primes

print str(sum(primes.create_primes(2 * 1000 * 1000)))