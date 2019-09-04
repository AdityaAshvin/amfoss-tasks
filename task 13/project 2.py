T = int(input())
s=0
se=0
for i in range(T):
    n = int(input())
    a=0
    b=1
    for j in range(1,n):
        s=s+b+a
        if(s%2==0):
            se=se+s
    print(se)     
    a=b
    b=s
    
s=0
se=0
