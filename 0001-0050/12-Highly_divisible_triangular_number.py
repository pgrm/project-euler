"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import math


def get_number_of_divisors(number):
    sqrt_number = int(math.sqrt(number))
    num_of_divisors = 0

    for d in xrange(1, sqrt_number + 1):
        if number % d == 0:
            num_of_divisors += 2

    # if sqrt(number) is an integer, than it has been added 2 and needs to be removed once
    if sqrt_number * sqrt_number == number:
        num_of_divisors -= 1

    return num_of_divisors


triangleNumber = 1  # ex. 1, 3, 6, 10, 15, 21, 28
i = 1  # ex. 1, 2, 3, 4, 5, 6, 7
while True:
    numOfDivisors = get_number_of_divisors(triangleNumber)
    if numOfDivisors > 500:
        break
    i += 1
    triangleNumber += i

print str(triangleNumber)