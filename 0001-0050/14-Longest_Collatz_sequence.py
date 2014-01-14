"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

chainLengths = {}
longestChain = 0
longestChainStartingNumber = 0

def get_next_collatz_number(number):
    if number % 2 == 0:
        return number / 2
    else:
        return number * 3 + 1


def get_collatz_chain_length(number):
    chain_length = 0
    original_number = number

    while number > 1:
        if number in chainLengths:
            chain_length += chainLengths[number]
            break
        else:
            number = get_next_collatz_number(number)
            chain_length += 1

    chainLengths[original_number] = chain_length
    return chain_length


for i in xrange(2, 1000 * 1000):
    currentLength = get_collatz_chain_length(i)

    if currentLength > longestChain:
        longestChain = currentLength
        longestChainStartingNumber = i

print str(longestChainStartingNumber)