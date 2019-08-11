n,k = map(int,input().split())
s = list(map(int,input().split()))
test = s[k-1]
cnt = 0
for i in range(0,len(s)):
    if(s[i] >= test and s[i]>0):
        cnt = cnt+1
print(cnt)



