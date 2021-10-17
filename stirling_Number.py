def stirling(n,k):
    n1=n
    k1=k
    if n<=0:
        return 1
     
    elif k<=0:
        return 0
     
    elif (n==0 and k==0):
        return -1
     
    elif n!=0 and n==k:
        return 1
     
    elif n<k:
        return 0
 
    else:
        temp1=stirling(n1-1,k1)
        temp1=k1*temp1
        return (k1*(stirling(n1-1,k1)))+stirling(n1-1,k1-1)
