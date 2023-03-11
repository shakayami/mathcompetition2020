from fractions import Fraction
hazure=4
atari=2
ALL=hazure+atari
X=[]
Y=[Fraction(1,1)]
for i in range(hazure+1):
    X.append(Y[-1]*Fraction(atari,ALL-i))
    Y.append(Y[-1]*Fraction(hazure-i,ALL-i))
print(X)
'''
X[i-1]:i回目でちょうどゲームが終わる確率
Y[i]:i回目でも終わらない確率
ゲームは5回目終了までには確実に終わる

'''
N=hazure+1
C=[]
ans=1
for s in range(1<<N):
    A=0
    B=0
    for i in range(N):
        if s>>i&1:
            A+=X[i]
        else:
            B+=X[i]
    ans=min(ans,abs(A-B))
print(ans)
for s in range(1<<N):
    A=0
    B=0
    for i in range(N):
        if s>>i&1:
            A+=X[i]
        else:
            B+=X[i]
    if abs(A-B)==ans:
        print([s>>i&1 for i in range(N)])


