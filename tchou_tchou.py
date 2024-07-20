x = int(input("What is the size of your train? "))
if (x < 0):
    print("Don't be so negative.")
elif (x > 0):
    row11 = ' '+25*'_'+' '*2
    row22 = '|]||[]_[]_[]|||[]_[]_[]||[| '
    row33 = '\\==o-o======o-o======o-o==/'
    row1 = ''
    row2 = ''
    row3 = ''
    row111 = ' '+22*'_' + '>' + '_'*2
    # print(row1,row2,row3,sep='\n')
    for i in range(1, x+1):
        if (i == x):
            row1 += row111
            row2 += row22
            row3 += row33
        else:
            row1 += row11
            row2 += row22
            row3 += row33+'_'

    print(row1, row2, row3, sep='\n')
