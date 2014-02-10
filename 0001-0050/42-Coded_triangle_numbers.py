"""
The n^th term of the sequence of triangle numbers is given by, tn = 1/2 n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

triangleNumbers = {}
highestTriangleNumber = 0
zeroValue = ord('A') - 1


def is_triangle_word(word_to_check):
    value = calculate_number_value(word_to_check)
    return is_triangle_number(value)


def calculate_number_value(word_to_calculate):
    return sum(ord(c) - zeroValue for c in word_to_calculate)


def is_triangle_number(number):
    if number > highestTriangleNumber:
        calculate_triangle_numbers(number)

    return number in triangleNumbers


def calculate_triangle_numbers(highest_number):
    global triangleNumbers
    global highestTriangleNumber

    next_triangle_index = len(triangleNumbers)
    while True:
        triangle_number = 0.5 * (next_triangle_index * (next_triangle_index + 1))
        triangleNumbers[triangle_number] = True
        next_triangle_index += 1
        highestTriangleNumber = triangle_number

        if highestTriangleNumber > highest_number:
            break


wordsFile = open('words.txt')
allWords = wordsFile.readline()
wordsFile.close()

allWords = allWords.replace('"', '')
words = sorted(allWords.split(','))

print str(len([1 for word in words if is_triangle_word(word)]))