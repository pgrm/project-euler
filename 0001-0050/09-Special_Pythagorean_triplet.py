"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

a = 0
b = 1


def c():
    return 1000 - (a + b)


def is_pythagorean_triplet():
    return (a * a) + (b * b) == c() * c()


while True:
    if is_pythagorean_triplet():
        break

    b += 1
    if c() <= b:
        a += 1
        b = a + 1

print str(a * b * c())