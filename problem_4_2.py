from fractions import Fraction
from collections import defaultdict
from bisect import bisect_left,bisect_right
import time
start=time.time()
hazure=40
atari=10
ALL=hazure+atari
X=[]
Y=[Fraction(1,1)]
geta=1
for i in range(ALL,hazure,-1):
    geta*=i
for i in range(atari):
    geta//=i+1
for i in range(hazure+1):
    X.append(Y[-1]*Fraction(atari,ALL-i))
    Y.append(Y[-1]*Fraction(hazure-i,ALL-i))

N=len(X)
X=[geta*x for x in X]
for x in X:
    assert x.denominator==1
X=[int(x) for x in X]
X_1=[]
X_2=[]
for i in range(N):
    if i%2==0:
        X_1.append(X[i])
    else:
        X_2.append(X[i])
N_1=len(X_1)
N_2=len(X_2)
S_1=[]
S_2=[]

D_1=defaultdict(list)
D_2=defaultdict(list)

for s in range(1<<N_1):
    tmp=0
    for i in range(N_1):
        if s>>i&1:
            tmp+=X_1[i]
        else:
            tmp-=X_1[i]
    D_1[tmp].append(s)
    S_1.append(tmp)

for s in range(1<<N_2):
    tmp=0
    for i in range(N_2):
        if s>>i&1:
            tmp+=X_2[i]
        else:
            tmp-=X_2[i]
    D_2[tmp].append(s)
    S_2.append(tmp)
S_1.append(-sum(X_1)*2)
S_1.append(sum(X_1)*2)

S_1.sort()
ans=sum(X)
for y in S_2:
    i=bisect_left(S_1,-y)
    for x in [S_1[i],S_1[i-1]]:
        ans=min(ans,abs(x+y))

print(Fraction(ans,geta))

for y in S_2:
    i=bisect_left(S_1,-y)
    for x in [S_1[i],S_1[i-1]]:
        if abs(x+y)==ans:
            for a in D_1[x]:
                for b in D_2[y]:
                    res=[0 for i in range(N)]
                    for i in range(N_1):
                        if a>>i&1:
                            res[2*i]=1
                    for i in range(N_2):
                        if b>>i&1:
                            res[2*i+1]=1
                    print(res)
                    c=0
                    for i in range(N):
                        if res[i]==0:
                            c+=X[i]
                        else:
                            c-=X[i]
                    assert abs(c)==ans,(abs(c),ans)

end=time.time()
print("Execution time : ",end-start)

'''
ゲームが終わるまでの最大回数はN=41なので、2^N回全探索すると間に合わない。
よって、半分全列挙で探索する。このとき計算量はO(2^(N/2)*poly(N))なので現実的な時間で計算できる。
実行結果の1行目は達成可能な確率の差の最小値である。
1行目が0ということはつまり、勝率を1/2:1/2にすることが可能ということである。

で、実行結果の2行目以降は勝率を1/2:1/2となるような割当パターンのリストである。
最小値を達成するような割当パターンは1706通り存在する。
また、実行結果の最後の行はこのプログラムの実行にかかった時間である。

'''
