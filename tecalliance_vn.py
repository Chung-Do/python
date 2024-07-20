x = int(input('Value?'))
for i in range(1, x):
    if (i % 5 == 0 and i % 9 == 0):
        print("Tecalliance_VN")
    elif (i % 5 == 0):
        print("Tecalliance")
    elif (i % 9 == 0):
        print("VN")
    else:
        print(i)
