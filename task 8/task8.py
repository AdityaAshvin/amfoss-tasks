try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract import image_to_string

x = pytesseract.image_to_string(Image.open('./Home/Desktop/cap.png'))
n1 = int(x[0:1])
n2 = int(x[2:3])
if '/' in x:
    div = n1/n2
    print(div)
elif '+' in x:
    su = n1+n2
    print(su)
elif '-' in x:
    sub = n1-n2
    print(sub)
elif '*' in x:
    mul = n1*n2
    print(mul)

    



