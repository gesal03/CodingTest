import sys
input = sys.stdin.readline

n, k = map(int, input().split())
k-=1
intList = list(range(1,n+1))
answerList=[]
index = k
while(True):
    if len(intList) == 1:
        answerList.append(intList.pop())
        break
    if index >= len(intList):
        index %= len(intList)
    answerList.append(intList.pop(index))
    index += k

print("<", end="")
for item in answerList:
    if item == answerList[len(answerList)-1]:
        print(item, end="")
    else:
        print(str(item) + ",", end=" ")
print(">")