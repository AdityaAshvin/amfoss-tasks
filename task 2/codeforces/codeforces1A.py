n,m,a = map(int,input( ).split())
if(n%a == 0):      #rowwise
    b = (n//a)
else:
    b = ((n//a)+1)
 
if(m%a == 0):      #columnwise
    c = (m//a)
else:
    c = ((m//a)+1)
 
print(b*c)     #printing number of flagstones req

