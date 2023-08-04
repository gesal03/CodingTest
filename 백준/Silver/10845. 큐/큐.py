import sys
import math
from collections import deque
input = sys.stdin.readline

loop = int(input())
deq = deque()

def push(x):
    deq.append(x)

def pop():
    if empty() == 1:
        return -1
    else:
        return deq.popleft()

def size():
    return len(deq)

def empty():
    if size() == 0:
        return 1
    else:
        return 0

def front():
    if empty() == 1:
        return -1
    else:
        return deq[0]

def back():
    if empty() == 1:
        return -1
    else:
        return deq[len(deq)-1]

for _ in range(loop):
    met = input()
    if "push" in met:
        met,x = met.split(" ")
        x = int(x)
        push(x)
    elif "pop" in met:
        print(pop())
    elif "size" in met:
        print(size())
    elif "empty" in met:
        print(empty())
    elif "front" in met:
        print(front())
    elif "back" in met:
        print(back())
    else:
        pass
        # print("nah")