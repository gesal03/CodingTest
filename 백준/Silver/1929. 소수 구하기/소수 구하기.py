import sys
import math
input = sys.stdin.readline

a, b = input().split()
a=int(a)
b=int(b)

for num in range(a, b+1):
    isPrime = True
    if num == 1:
        isPrime = False
    max = int(num ** 0.5)
    for i in range(2, max+1):
        if num % i == 0:
            isPrime=False
            break
    if isPrime:
        print(num)