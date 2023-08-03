import sys
input = sys.stdin.readline
loop = int(input())

arr=[]
for _ in range(loop):
    num = int(input())
    arr.append(num)
arr.sort()
for i in arr:
    print(i)
