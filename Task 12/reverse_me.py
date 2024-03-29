import string


def xor(x):
    return ''.join(chr(ord(i)^10) for i in x)


def shift(x):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    n = []
    for i in x:
        if i.isupper() is True:
            n.append(upper[(upper.index(i)+3)%26])
        elif i.islower() is True:
            n.append(lower[(lower.index(i)+3)%26])
        elif i.isdigit() is True:
            n.append(digits[(digits.index(i)+3)%10])
    return n

def encode(x):
    return x.encode("hex")

def Shifting(x):
    l = string.ascii_lowercase
    u = string.ascii_uppercase
    length = string.digits
    a = []
    for i in x:
        if i.islower() is True:
            a.append(lower[(lower.index(i)-3)%26])
        elif i.islower() is True:
            a.append(lower[(lower.index(i)-3)%26])
        elif i.isdigit() is True:
            a.append(digits[(digits.index(i)-3)%10])
    return a

def decode(a):
    return a.decode("hex")


if __name__=="__main__":
    print("Decode the following string to find the flag:")
    print("667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268")
    decoded = Shifting(xor(decode("667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268")))
    your_code = encode(xor(shift(decoded)))

if your_code == "667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268":
           print("Yeah!....You are a Genius")
else:
           print("Oops....Try again")
           print("Looking at the source code might help")
