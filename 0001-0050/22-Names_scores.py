"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

namesFile = open('names.txt')
allNames = namesFile.readline()
namesFile.close()

allNames = allNames.replace('"', '')
names = sorted(allNames.split(','))

sumOfScoreOfNames = 0
valueOfA = ord('A')
i = 0

for name in names:
    i += 1
    sumOfCharsInName = 0
    for c in name:
        sumOfCharsInName += (ord(c) - valueOfA + 1)

    scoreOfName = sumOfCharsInName * i
    sumOfScoreOfNames += scoreOfName

print str(sumOfScoreOfNames)