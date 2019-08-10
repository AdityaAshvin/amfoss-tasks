array = []
i = 0
cnt = 0
nn = int(input("enter a number "))
for i in range(nn):
    a = int(input(" enter heights of the candles "))
    array.append(a)
    big = array[i]
for i in range(nn):
        if (array[i] >= big):
            cnt = cnt+1

print(cnt)
s
