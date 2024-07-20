row = int(input())
colInRow = row*3
pattern = '.|.'
middleRowText = 'WELCOME'
middleRowIndex = (row-1)/2

for rowIndex in range(row):
    if(rowIndex == middleRowIndex):
        numberOfSpaceNeedToAddInTwoSide = int((colInRow - 7)/2)

        print(numberOfSpaceNeedToAddInTwoSide*'-'+middleRowText+numberOfSpaceNeedToAddInTwoSide*'-', end="\n")
    else:
        absValueToMiddleRow = int(abs(middleRowIndex-rowIndex))
        numberOfPatternInRow = int(middleRowIndex - absValueToMiddleRow + 1)
        numberOfSpaceNeedToAddInTwoSide = int((colInRow - 3*numberOfPatternInRow)/2)
        print(numberOfSpaceNeedToAddInTwoSide*'-' + numberOfPatternInRow*pattern + numberOfSpaceNeedToAddInTwoSide*'-', end="\n")