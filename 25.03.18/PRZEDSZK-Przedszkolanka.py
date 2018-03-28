def funkcja(tt):
        wynik=[]
        for i in range(tt):
                lista=input()
                lista=lista.split()
                if(int(lista[0])<10 or int(lista[1])>30):
                        return exit()
                ab=int(lista[0])*int(lista[1])
                from fractions import gcd
                nwd=gcd(int(lista[0]),int(lista[1]))
                nww=int(lista[0])/nwd*int(lista[1])
                wynik.append(str(int(nww)))
                wynik.append("\n")
        print(''.join(wynik))
        return exit()

t=int(input())
if(t<0 or t>20):
        exit()
print(funkcja(t))
