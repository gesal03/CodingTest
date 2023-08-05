import sys
input = sys.stdin.readline


n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))
card_count = {}

for i in mList:
    card_count[i] = 0

for i in nList:
    if i in card_count.keys():
        card_count[i]+=1

for i in mList:
    print(card_count[i], end=' ')