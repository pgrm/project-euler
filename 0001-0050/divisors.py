"""
not part of project-euler just a helper function to create list of divisors which are necessary for multiple solutions
"""

def get_proper_divisors(number):
    divisor = 0
    divisors = []

    while True:
        divisor += 1
        quotient = number / divisor

        if divisor > quotient:
            break

        if number % divisor == 0:
            divisors += [divisor]
            if divisor != quotient and quotient < number:
                divisors += [quotient]

    return divisors