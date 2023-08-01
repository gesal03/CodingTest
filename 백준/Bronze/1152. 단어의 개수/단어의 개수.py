str = input()
str = str.strip()
if str=="":
    print("0")
else:
    strList = str.split(" ")
    print(len(strList))
