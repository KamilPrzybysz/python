import math
class Prostokat:
    def funkcja(self):
        x=int(input("Podaj wspolrzedna X wierzcholka: "))
        y=int(input("Podaj wspolrzedna Y wierzcholka: "))
        h=int(input("Podaj wysokosc: "))
        w=int(input("Podaj szerokosc: "))
        obwod=h*2+w*2
        pole=h*w
        srodekx=x+w/2
        srodeky=y+h/2
        print("Obwod to "+str(obwod)+", pole to "+str(pole)+", wspolrzedne srodka to ("+str(srodekx)+","+str(srodeky)+")")

mojaklasa=Prostokat()
mojaklasa.funkcja()
