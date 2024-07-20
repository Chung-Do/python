
# Approach#2

def findReverseNumber2(n: int):
    def hasNoSimilarDigit(a): return len(str(a)) == len(set(str(a)))
    for k in range(2, 10):
        for i in range(10**(n-1), int(10**n / k)):
            last_digit = i % 10
            first_digit = int(i / 10**(n-1))
            if ((last_digit * k) % 10 != first_digit):
                break
    return

# Approach#1

def findReverseNumber(n: int) -> str:
    reverseNo_arr = []
    def isReverseNumber(a, b): return str(a) == str(b)[::-1]
    def hasNoSimilarDigit(a): return len(str(a)) == len(set(str(a)))

    # k in [2,9]
    for k in range(2, 10):
        for i in range(10**(n-1), int(10**n/k)):
            if (hasNoSimilarDigit(i)):
                    if (i*k >= 10**n):
                        break
                    elif isReverseNumber(i, i*k):
                        reverseNo_arr.append((i, k))
    return str(reverseNo_arr)


if __name__ == "__main__":
    n = int(input('Enter length of number: '))
    if (n < 2 or n > 10):
        print('Invalid n (n must be > 1 and <= 10)')
    else:
        print('Reverse numbers: ' + findReverseNumber(n))
