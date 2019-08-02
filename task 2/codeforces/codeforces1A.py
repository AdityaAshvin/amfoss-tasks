n,m,a = map(int,input( "enter n, m and a where n*m is the size of the rectangular field and a*a is the size of the flagstones ").split())
if(n%a == 0):      #rowwise
    b = (n//a)
else:
    b = (n//(a+1))

if(m%a == 0):      #columnwise
    c = (m//a)
else:
    c = (m//(a+1))

print(b*c)     #printing number of flagstones req
