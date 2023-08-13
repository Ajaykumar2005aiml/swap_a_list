n=int(input())
N=list(map(int,input().split()))
a=0
b=1
for i in range(len(N)):
    if a < len(N)-1:
        c=N[a]
        N[a]=N[b]
        N[b]=c
        a=b+1
        b=a+1
    else:
        break
print(*N)
