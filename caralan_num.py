import math
def catalan(n): # 반만 만들어놓으면 나머지반은 고정이니까!
    return math.factorial(2*n) // (math.factorial(n)*math.factorial(n+1))
a=int(input())
n=[]
for i in range(a):
    n.append(int(input()))
for i in n:
    if i % 2 ==1:
        print(0)
    else:
        print(catalan(i//2)%1000000007)
