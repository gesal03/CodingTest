loop = int(input())
intList = input().split()
count=0
for num in intList:
    num = int(num)
    isPrime=True
    if num == 1:
        isPrime=False
    for i in range(2, num-1):
        if num % i == 0:
            isPrime=False
            break
    if isPrime:
        count+=1
print(count)