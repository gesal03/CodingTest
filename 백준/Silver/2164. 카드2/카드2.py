import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

deq = deque(range(1,n+1))

# arr=list(range(1,n+1))

while(len(deq)>1):
    deq.popleft()
    deq.rotate(-1)

print(deq[0])
