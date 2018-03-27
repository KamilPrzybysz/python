def funkcja(dd):
        wynik=[]
        for i in range(dd):
                silnia=1
                n=int(input())
                if(n<0 or n>1000000000):
                        exit()
                elif(n>=10):
                    wynik.append(str(0))
                    wynik.append(str(" "))
                    wynik.append(str(0))
                    wynik.append(str('\n'))
                else:
                    for j in range(1,(n+1)):
                            silnia=int(silnia)*int(j)
                    dziesiec=int((silnia%100)/10)
                    jednosc=int(silnia%10)
                    wynik.append(str(dziesiec))
                    wynik.append(str(" "))
                    wynik.append(str(jednosc))
                    wynik.append(str('\n'))
        return ''.join(wynik)

d=int(input())
if(d<1 or d>30):
        exit()
print(funkcja(d))
