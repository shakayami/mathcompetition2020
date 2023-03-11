def digitsum(n):
    res=0
    for i in str(n):
        res+=int(i)
    return res

MAX_N=10**4

G=[[] for i in range(37)]
for i in range(1,MAX_N+1):
    G[digitsum(i)].append(i)
ans=[len(seq) for seq in G]
MAX_LEN=max(ans)
print(ans)
for i in range(37):
    if ans[i]==MAX_LEN:
        print(i,ans[i])

