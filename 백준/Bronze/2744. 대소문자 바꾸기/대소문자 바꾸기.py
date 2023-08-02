str = input()
a=""
for ch in str:
    if ch.isupper():
        a+=ch.lower()
    else:
        a+=ch.upper()
print(a)