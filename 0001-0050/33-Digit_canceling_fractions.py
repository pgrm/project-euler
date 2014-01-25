"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from fractions import Fraction


def without(pair, exclude):
    if pair[0] == exclude:
        return pair[1]
    else:
        return pair[0]


correctFractions = []

for denominator in xrange(11, 100):
    if denominator % 10 == 0:
        continue

    for numerator in xrange(11, denominator):
        if numerator % 10 == 0:
            continue

        fraction = Fraction(numerator, denominator)

        nums = (numerator / 10, numerator % 10)
        dens = (denominator / 10, denominator % 10)

        if nums[0] in dens:
            if fraction == Fraction(nums[1], without(dens, nums[0])):
                correctFractions += [fraction]
        elif nums[1] in dens:
            if fraction == Fraction(nums[0], without(dens, nums[1])):
                correctFractions += [fraction]

finalProduct = Fraction(1, 1)

for f in correctFractions:
    finalProduct *= f

print str(finalProduct)