loop = int(input())

xList=[]
yList=[]
countList=[]
for _ in range(loop):
    line = input() 
    xy = line.split(" ")
    x = int(xy[0])
    y = int(xy[1])

    xList.append(x)
    yList.append(y)

for i in range(loop):
    count=1
    x = xList[i]
    y= yList[i]

    for i in range(loop):
        if x < xList[i]:
            if y < yList[i]:
                count+=1
    countList.append(count)

for a in countList:
    print(a, end=" ")

