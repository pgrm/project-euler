"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number
that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

import permutations

allPermutations = set([permutations.combine_numbers(x) for x in permutations.permutations(range(1, 10))])
highestNumber = 0

for n in xrange(1, 10000):  # the was found experimentally
    pandigitalMultiply = 0

    for i in xrange(1, 10):
        pandigitalPart = n * i
        pandigitalMultiply *= (10 ** len(str(pandigitalPart)))
        pandigitalMultiply += pandigitalPart

        if len(str(pandigitalMultiply)) >= 9:
            break

    if pandigitalMultiply in allPermutations:
        if pandigitalMultiply > highestNumber:
            highestNumber = pandigitalMultiply

print str(highestNumber)