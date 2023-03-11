def solve(m):
    X=[1 for i in range(10)]
    A=[1]
    for i in range(m):
        B=[0 for i in range(len(A)+len(X)-1)]
        for i,x in enumerate(X):
            for j,y in enumerate(A):
                B[i+j]+=x*y
        A=B
    return A

def binomial(n,k):
    if (0<=k and k<=n):
        res=1
        for i in range(k):
            res*=n-i
            res//=i+1
        return res
    else:
        return 0

for m in range(2,30):
    A=solve(m)
    i=max([(a,i) for i,a in enumerate(A)])[1]
    j=(9*m+1)//2
    print(m,max(A),i,j)
