"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the n-th digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

desiredIndices = [0, 9, 99, 999, 9999, 99999, 999999]

constant = ''
i = 1
product = 1

while len(constant) <= desiredIndices[-1]:
    constant += str(i)
    i += 1

for j in desiredIndices:
    product *= int(constant[j])

print str(product)