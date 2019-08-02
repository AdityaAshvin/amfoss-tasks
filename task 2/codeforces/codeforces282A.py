n = int(input(" enter a number "))
x = 0
for test in range(n):
    test = input(" enter ++x for incresing the value or --x for decreasing the value ")
    if (test[1] == "+"):
        x = x+1
    else:
        x = x-1

print(x)
