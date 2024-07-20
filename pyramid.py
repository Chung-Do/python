import math
s = int(input())

if(s <= 0):
    print("invalid")
elif s == 1 or s == 2:
    print("#")
else:
    h = math.ceil(s/2)
    print("height:", h)
    for r in range(h-1):
        i = r + 1
        row_i = " "*(h-i) + "#"*(2*i-1) + " "*(h-i)
        print(row_i)
    print("#"*s)
