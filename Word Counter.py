import os
import re
os.chdir('C:\\Users\\Jack\\Documents\\Programming Projects\\..Python')
print('Current Directory: ' + os.getcwd())
testFile = open('Input.txt')
testRead = testFile.read()
testFile.close()
print(testRead)
sent = re.split('[;.!?…]',testRead)
word = re.split('[;.,!?… \n\t\r\\/(){}\[\]\<\>~\"]',testRead)
common = {}
sent = list(filter(None, sent))

word = list(filter(None, word))
char = list(testRead)

for x in word:
    toAdd = {}
    x = list(x.lower())
    x[0] = x[0].upper()
    x = "".join(x)
    if (x in common):
        toAdd.update({x : common[x] + 1})
    else:
        toAdd.update({x : 1})
    common.update(toAdd)
common = list(common.items())
for x in range(0, len(common)):
    maxi = 0
    index = 0
    temp = ('temp', 0)
    for y in range(x, len(common)):
        if (common[y][1] > maxi):
            maxi = common[y][1]
            index = y
    temp = common[x]
    common[x] = common[index]
    common[index] = temp

print('\nThere are ' + str(len(sent)) + ' sentences with ' + str(len(word)) + ' words ' + 'and ' + str(len(char)) + ' characters')
if (len(common) < 10):
    print('\nTop ' + str(len(common)) + ' most common words:')
    for x in range(0, len(common)):
        print(str(common[x][0]) + ': ' + str(common[x][1]))
else:
    print('\nTop 10 most common words:')
    for x in range(0, 10):
        print(str(common[x][0]) + ': ' + str(common[x][1]))
