try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract import image_to_string

x = pytesseract.image_to_string(Image.open('./Home/Desktop/cap'))
n1 = int(x[0:1])
n2 = int(x[2:3])
if '+' in x:
    y = n1+n2
    print(y)
elif '-' in x:
    y = n1-n2
    print(y)
elif '*' in x:
    y = n1*n2
    print(y)
elif '/' in x:
    y = n1/n2
    print(y)

    



