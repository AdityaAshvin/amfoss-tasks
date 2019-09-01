def rawinput():
 a = int(raw_input())
 difference = 0
 for i in range(1,a):
    row = raw_input().split()
    difference = difference + (int(row[i]) - int(row[a-1-i]))
 print(abs(difference))
