import math


def isPrime(number):
    Prime = True

    if number == 1:
        Prime = False
    elif number % 2 == 0:
        Prime = False

    for i in range(3, math.floor(math.sqrt(number))+2, 2):
        if number % i == 0:
            Prime = False
            break

    return Prime


T = int(input())

array = []

for i in range(T):
    array.append(int(input()))

for i in range(len(array)):
    for j in range(1, array[i]*2):
        if isPrime(j) and isPrime(array[i]*2-j):
            print(str(j) + " " + str(array[i]*2-j))
            break
