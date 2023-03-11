#解法1
H=5
W=6
stack=[(0,0)]
path=[]
def dfs():
    if stack[-1]==(H-1,W-1):
        path.append(stack[:])
    x,y=stack[-1]
    if x+1<H:
        stack.append((x+1,y))
        dfs()
        stack.pop()
    if y+1<W:
        stack.append((x,y+1))
        dfs()
        stack.pop()
    if x+1<H and y+1<W:
        stack.append((x+1,y+1))
        dfs()
        stack.pop()

#ありうるパスを全列挙する
dfs()
ans_prob_1_1=681
assert len(path)==ans_prob_1_1

ans=0
for seq in path:
    dp=[[0 for j in range(W)]for i in range(H)]
    is_passable=[[True for j in range(W)]for i in range(H)]
    for x,y in seq:
        is_passable[x][y]=False
    is_passable[0][0]=True
    is_passable[H-1][W-1]=True
    dp[H-1][W-1]=1
    for i in range(H-1,-1,-1):
        for j in range(W-1,-1,-1):
            if i+1<H:
                dp[i][j]+=dp[i+1][j]
            if j+1<W:
                dp[i][j]+=dp[i][j+1]
            if i+1<H and j+1<W:
                dp[i][j]+=dp[i+1][j+1]
            if not(is_passable[i][j]):
                dp[i][j]=0
    ans+=dp[0][0]
print(ans)
