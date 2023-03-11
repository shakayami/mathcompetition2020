from functools import lru_cache
def generate(a,b,c):
    res=[[1 for j in range(a)]for i in range(b)]
    for j in range(c):
        res[-j-1][0]=0
    return res

figure_5=generate(3,6,0)
figure_6=generate(3,6,3)
figure_7=generate(19,8,0)
figure_8=generate(19,8,3)
figure_9=generate(5,8,2)


def solve(board):
    H=len(board)
    W=len(board[0])
    B=[[0 for j in range(W)]for i in range(H+1)]
    C=[[0 for j in range(W+1)]for i in range(H+1)]
    for i in range(H):
        for j in range(W):
            B[i+1][j]=B[i][j]+board[i][j]
    for i in range(H+1):
        for j in range(W):
            C[i][j+1]=C[i][j]+B[i][j]
    def chocolate_size(il,ir,jl,jr):
        return C[il][jl]+C[ir][jr]-C[il][jr]-C[ir][jl]
    def next_route(il,ir,jl,jr):
        res=set()
        for im in range(il+1,ir):
            cost_A=chocolate_size(il,im,jl,jr)
            cost_B=chocolate_size(im,ir,jl,jr)
            if min(cost_A,cost_B)==0:
                continue
            if cost_A<=cost_B:
                res.add((im,ir,jl,jr))
            if cost_B<=cost_A:
                res.add((il,im,jl,jr))
        for jm in range(jl+1,jr):
            cost_A=chocolate_size(il,ir,jl,jm)
            cost_B=chocolate_size(il,ir,jm,jr)
            if min(cost_A,cost_B)==0:
                continue
            if cost_A<=cost_B:
                res.add((il,ir,jm,jr))
            if cost_B<=cost_A:
                res.add((il,ir,jl,jm))
        return res
    @lru_cache(maxsize=10**8)
    def grundy(il,ir,jl,jr):
        if chocolate_size(il,ir,jl,jr)<=1:
            return 0
        S=set()
        for a,b,c,d in next_route(il,ir,jl,jr):
            S.add(grundy(a,b,c,d))
        i=0
        while(i in S):i+=1
        return i
    
    ans=grundy(0,H,0,W)
    for a,b,c,d in next_route(0,H,0,W):
        if grundy(a,b,c,d)==0:
            print(a,b,c,d)
    return ans

print(solve(figure_5))
print(solve(figure_6))
print(solve(figure_7))
print(solve(figure_8))

'''
grundy数が0なら後手必勝
0以外なら先手必勝

状態は[il,ir)*[jl,jr)の範囲だけ残ったときのgrundy数を考える

'''
