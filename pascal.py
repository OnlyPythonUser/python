rows = int(input("파스칼의 삼각형을 출력할 행의 개수를 입력하세요> "))
lst=[]

for i in range(rows):
    lst.append([])
    lst[i].append(1)
    
    for j in range(1, i):
        lst[i].append(lst[i-1][j-1]+lst[i-1][j])
        
    if(rows != 0):
        lst[i].append(1)
        
for i in range(rows):
    print("   " * (rows - i), end=" ", sep=" ")
    for j in range(0, i+1):
        print('{0:6}'.format(lst[i][j]), end=" ", sep=" ")
    print()
print("===================================================================")
pascal = [[1 for _ in range(i)] for i in range(1, 31)]

for i in range(2, 30):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

n, k = map(int, input().split())
print(pascal[n-1][k-1])
