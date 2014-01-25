"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import permutations

foundProducts = {}
foundProductsSum = 0

for perm in permutations.permutations(range(1, 10)):
    product = permutations.combine_numbers(perm[-4:])  # last four digits

    for x in xrange(1, 4):
        factor1 = perm[:x]  # first x digit
        factor2 = perm[x:-4]  # starting from x'th digit + 1 (0-based index) all except the last four

        factor1 = permutations.combine_numbers(factor1)
        factor2 = permutations.combine_numbers(factor2)

        if factor1 * factor2 == product:
            if product not in foundProducts:
                foundProductsSum += product
                foundProducts[product] = 1
            #print str(factor1) + " x " + str(factor2) + " = " + str(product)

print str(foundProductsSum)