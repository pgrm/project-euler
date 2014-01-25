"""
not part of project-euler just a helper function to create permutations which are necessary for multiple solutions
"""


def split_into_digits(number):
    digits = []

    while number > 0:
        digits = [number % 10] + digits
        number /= 10

    return digits


def combine_numbers(numbers):
    i = len(numbers)
    combined_number = 0

    for n in numbers:
        i -= 1
        combined_number += n * (10 ** i)

    return combined_number


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

