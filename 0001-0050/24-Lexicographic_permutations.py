"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


def exchange_values_at_indices(items, index1, index2):
    tmp = items[index1]
    items[index1] = items[index2]
    items[index2] = tmp


def permutations(items, index=0):
    if index == len(items):
        yield list(items)
    else:
        for i in xrange(index, len(items)):
            exchange_values_at_indices(items, i, index)
            for permutation in permutations(items, index + 1):
                yield permutation
            exchange_values_at_indices(items, i, index)


print sorted(permutations(range(0, 10)))[1000*1000 - 1]