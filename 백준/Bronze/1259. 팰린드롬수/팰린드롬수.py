import sys
from collections import deque
# input = sys.stdin.readline

deq = deque()

while(True):
    strList = input()
    if strList == "0":
        break 
    isRight=True
    deq = deque(strList)
    while(len(deq) > 1):
        start = deq.popleft()
        end = deq.pop()
        if start != end:
            isRight=False
            break
    if isRight:
        print("yes")
    else:
        print("no")
