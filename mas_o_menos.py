result = input('What is the result? ')
while (result.isdigit() == False ):
    result = input('Please input number only: ')
result = int(result)
for i in range(11):
    x = input('Your guess? ')
    while(x.isdigit() == False): x = input('Please re-input your guess, must be number: ')
    x = int(x)
    if (x<result):
        if(result - x) >50: print("It's way more")
        else: print("It's more")
    elif(x>result):
        if(x-result) >50: print("It's way less")
        else: print("It's less")
    else: print("congrats !")
print("you lose :(")

    