string1 = input()
if (string1[-2:] == "AM" and string1[ :2] == "12"):
    print( "00" + string1[2:-2])         #checking if the last two digits of the string is AM or PM and changing 12 with 00
elif (string1[-2: ] == "AM"):
    print(string1[ :-2])                 #dropping AM
elif (string1[-2:] == "PM" and string1[ :2] == "12"):
    print( "12" + string1[2:-2])
else:
    print(str(int(string1[:2]) + 12) + string1[2:8])      #printing in 24 hour format.

    

    


    

    
