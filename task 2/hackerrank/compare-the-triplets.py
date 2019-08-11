a = [int(a1) for a1 in input().split()]
b = [int(b1) for b1 in input().split()]
i = 0
alice = 0
bob = 0
for i in range(3):
    if(a[i]>b[i]):
        alice = alice+1
    elif(a[i]<b[i]):
        bob = bob+1
    else:
        alice=alice
        bob=bob

print(alice,bob)
        
