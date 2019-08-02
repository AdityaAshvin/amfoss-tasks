n,k = map(int,input(" enter number of participating students and then k-th position ").split())
s = list(map(int,input(" enter scores of the participants " ).split()))
test = s[k-1]
cnt = 0
for i in range(0,len(s)):
    if(s[i] >= test and s[i]>0):
        cnt = cnt+1
print(cnt)



