"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

from math import sqrt

numberOfSolutionPerPerimeter = {}


def c(a, b):
    return sqrt(a*a + b*b)


def calculate_perimiter(a, b):
    return a + b + c(a, b)


def add_solution_for_perimeter(p):
    if p in numberOfSolutionPerPerimeter:
        numberOfSolutionPerPerimeter[p] += 1
    else:
        numberOfSolutionPerPerimeter[p] = 1


a = 1
b = 1
highestNumberOfSolutions = 0
bestPerimeter = 0

while True:
    while True:
        perimeter = calculate_perimiter(a, b)

        if perimeter > 1000:
            break
        elif perimeter == int(perimeter):
            add_solution_for_perimeter(perimeter)

            if numberOfSolutionPerPerimeter[perimeter] > highestNumberOfSolutions:
                bestPerimeter = perimeter
                highestNumberOfSolutions = numberOfSolutionPerPerimeter[perimeter]

        b += 1

    a += 1
    b = a

    if calculate_perimiter(a, b) > 1000:
        break

print str(bestPerimeter)