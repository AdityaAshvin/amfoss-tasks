T = int(input())
s=0
for i in range(T):
    N = int(input())
    for j in range(1,N):
        if((j%3==0)or(j%5==0)):
            s=s+j
    print(s)
    
        
        
