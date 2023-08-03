n = input()
a = map(int, input().split())
aList = set(a)
m = input()
targetList = map(int, input().split())

for num in targetList:
    if num in aList:
        print(1)
    else:
        print(0)
