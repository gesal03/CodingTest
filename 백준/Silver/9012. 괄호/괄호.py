loop = int(input())
for _ in range(loop):
    line = input()
    countLeft=0
    count=0
    isStart=False
    for ch in line:
        if ch == '(':
            countLeft+=1
            count+=1
        elif ch==')':
            if countLeft != 0:
                count-=1
                countLeft-=1
            else:
                isStart=True
    if isStart == True:
        count=-1
    if count == 0:
        print("YES")
    else:
        print("NO")    