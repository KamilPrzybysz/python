nazwa=open('liczby.txt','w')
for i in range(11,21):
    nazwa.write(str(i)+'\n')
nazwa.close()
nazwa2=open('liczby.txt','r').read()
linie=nazwa2.split('\n')
for i in range(len(linie)-1):
    a=int(linie[i])
    wynik=a*a
    print(wynik)
