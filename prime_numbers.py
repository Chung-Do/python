import math
x = int(input("Let's print the prime numbers up to? "))
if x > 2:
    for i in range(2, x + 1):
        if all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)):
            print(i)
    #The "all" function returns True only if all elements of the generator expression are True, effectively checking if i is prime.