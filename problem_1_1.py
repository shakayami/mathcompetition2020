#解法1
H=5
W=6
dp=[[0 for j in range(W)]for i in range(H)]
dp[0][0]=1
for i in range(H):
    for j in range(W):
        if i>0:
            dp[i][j]+=dp[i-1][j]
        if j>0:
            dp[i][j]+=dp[i][j-1]
        if i>0 and j>0:
            dp[i][j]+=dp[i-1][j-1]
for line in dp:
    print(line)
print(dp[H-1][W-1])
print("#"*50)
#解法2

def fact(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

ans=0
for C in range(5):
    A=4-C
    B=5-C
    ans+=fact(A+B+C)//(fact(A)*fact(B)*fact(C))
    print(A,B,C,fact(A+B+C)//(fact(A)*fact(B)*fact(C)))
print(ans)


'''
下へ行くのをA回
右へ行くのをB回
右下に行くのをC回と回数を固定する。
このとき、A,B,Cは非負であり、
A+C=4
B+C=5
を満たす。
それぞれのA,B,Cについて(A+B+C)!/(A!B!C!)を足せば答えになる。
ここで、Cを定めればA,Bが定まるので、A,B,Cとしてあり得る組み合わせは
(A,B,C)=(4,5,0),(3,4,1),(2,3,2),(1,2,3),(0,1,4)
の5通り
で、答えは126+280+210+60+5=681通り



'''
