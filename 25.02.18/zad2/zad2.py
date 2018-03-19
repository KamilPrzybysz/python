wybor=input("Wybierz liczenie pola kola-1\nWybierz liczenie pola kwadratu-2\nWybierz liczenie pola prostokata-3\n")

import math
pole=0
if wybor==1:
    r=input("Podaj promien kola: ")
    pole=math.pi*r**2
elif wybor==2:
    a=input("Podaj bok kwadratu: ")
    pole=a*a
elif wybor==3:
    a=input("Podaj bok a: ")
    b=input("Podaj bok b: ")
    pole=a*b
else:
    exit()
print"Pole=",pole
