# n = int(input())
# m = n*3
# row = ''
# for i in range (n):
#     row += m*'-'
# print(row)

row = int(input())
# find number of col in row
col = 3*row

# find middle row index
middleRowIndex = (row-1)/2

#loop all of row
for rowIndex in range (row):
    rowVisulaization =""
    # print WELCOME in middle row
    for colIndex in range(col):
        if(rowIndex == middleRowIndex):
            middleCharacterIndex = (col-1)/2
            gapFromCurrentCharToMiddle = abs(colIndex-middleCharacterIndex)
            if(gapFromCurrentCharToMiddle>3):
                rowVisulaization+="-"
            if(middleCharacterIndex-colIndex ==3):
                rowVisulaization+="WELCOME"
            print('\n')    



        # else:
        #     # print gap between middle and the current row
        #     # print(abs(rowIndex-middleRowIndex),end="\n")
        #     #print number of pattern in line
        #     numberOfPattern = int(2*(middleRowIndex-abs(rowIndex-middleRowIndex)+1)-1)
        #     print(numberOfPattern*".|.", end='\n')
