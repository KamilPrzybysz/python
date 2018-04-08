import math
class Punkt:
    def funkcja(self):
        a=int(input("Podaj liczbe a: "))
        b=int(input("Podaj liczbe b: "))
        wynik=(a*a+b*b)
        wynik2=math.sqrt(wynik)
        print(wynik2)


mojaklasa=Punkt()
mojaklasa.funkcja()
