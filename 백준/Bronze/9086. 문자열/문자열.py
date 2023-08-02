loop = int(input())

for _ in range(loop):
    str = input()
    print(str[0], end="")
    print(str[len(str)-1])