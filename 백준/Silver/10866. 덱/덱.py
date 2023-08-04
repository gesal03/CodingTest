import sys
import math
from collections import deque
input = sys.stdin.readline

loop = int(input())

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

deq = deque()

def push_front(x):
    deq.appendleft(x)

def push_back(x):
    deq.append(x)

def pop_front():
    if empty() == 1:
        return -1
    else:
        return deq.popleft()

def pop_back():
    if empty() == 1:
        return -1
    else:
        return deq.pop()

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
    if "push_front" in met:
        met,x = met.split(" ")
        x = int(x)
        push_front(x)
    elif "push_back" in met:
        met,x = met.split(" ")
        x = int(x)
        push_back(x)
    elif "pop_front" in met:
        print(pop_front())
    elif "pop_back" in met:
        print(pop_back())
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