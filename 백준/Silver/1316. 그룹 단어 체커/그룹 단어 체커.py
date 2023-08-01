loop = int(input())

count=0
for _ in range(loop):
    str = input()
    strArr = list(str)
    before=''
    isCheck=True
    isCalled=[]
    for char in strArr:
        if before != char:
            if char in isCalled:
                isCheck=False
                break
            before = char
            isCalled.append(char)
    if isCheck:
        count+=1

print(count)