import math
strList = input()

dic = dict()
for i in range(0,9):
    key = str(i)
    dic[key] = 0

for ch in strList:
    if ch == '9':
        dic['6']+=1
    else:
        dic[ch]+=1
dic['6'] = math.ceil(dic['6'] / 2)
big=0
for value in dic.values():
    if value > big:
        big=value
print(big)