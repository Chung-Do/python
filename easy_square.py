size = int(input())
characters = input()
if (len(characters) != 5 or size < 1):
    print("Invalid value")
elif (size == 1):
    print(characters[0])
else:
    row1 = characters[0] + characters[1] * (size - 2) + characters[0]
    row2 = characters[3] + ' ' * (size - 2) + characters[4]
    row3 = characters[0] + characters[2] * (size - 2) + characters[0]

    print(row1)
    [print(row2) for _ in range(size - 2)]
    print(row3)
