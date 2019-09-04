T = int(input())
for i in range(T):
    n = int(input())
    cnt=0
    max=0
    for j in range(2,n):
        if(n%j==0):
            cnt=cnt+1
            k=j
        else:
            cnt=cnt
        if(cnt!=0):
            if(k>max):
                max = k
    print(max)


    
            
