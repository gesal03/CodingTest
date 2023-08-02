n,m = input().split()
n=int(n)
m=int(m)
arr1 =[[0 for col in range(m)] for row in range(n)]
arr2 =[[0 for col in range(m)] for row in range(n)]

# 첫 행렬
for i in range(n):
    intList = input().split()
    for j in range(m):
        arr1[i][j] = int(intList[j])

# 두번째 행렬
for i in range(n):
    intList = input().split()
    for j in range(m):
        arr2[i][j] = int(intList[j])

for i in range(n):
    for j in range(m):
        result = arr1[i][j] + arr2[i][j]
        if j == m-1:
            print(result)
        else:
            print(result, end=" ")