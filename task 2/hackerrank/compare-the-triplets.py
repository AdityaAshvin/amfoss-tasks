a = (input(" a(0) "),input(" a(1) "),input(" a(2) "))
b = (input(" b(0) "),input(" b(1) "),input(" b(2) "))
i = 0
alice = 0
bob = 0
for i in range(3):
    if(a[i]>b[i]):
        alice = alice+1
    elif(a[i]<b[i]):
        bob = bob+1
    else:
        alice=alice+1
        bob=bob+1
c = (alice,bob)
print(c)
        
