n = int(input(" enter a number "))
for i in range(n):
        word = input(" enter a word ")
        l = int(len(word))
        if (l > 10):
                first = word[0]
                last = word[l-1]
                final_word = (str(first)+str((l-2))+str(last))
                print(final_word)
        else:
                print(word)
