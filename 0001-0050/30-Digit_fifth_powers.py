"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 44
8208 = 8^4 + 2^4 + 0^4 + 84
9474 = 9^4 + 4^4 + 7^4 + 44
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def get_sum_of_fifth_power_digits(number):
    fifth_powered_sum = 0

    while number > 0:
        fifth_powered_sum += (number % 10) ** 5
        number /= 10

    return fifth_powered_sum


totalSum = 0

for i in xrange(10, 1000 * 1000):  # 1,000,000 was found as a border experimentally
    if i == get_sum_of_fifth_power_digits(i):
        totalSum += i

print str(totalSum)