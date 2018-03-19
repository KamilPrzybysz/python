def funkcja(wektor1, wektor2):
    iloczyn=0
    c=len(wektor1)
    for i in range(c):
        iloczyn+=wektor1[i]*wektor2[i]
    return iloczyn

a=int(input('Podaj dlugosc wektorow: '))
w1=[]
w2=[]
for i in range(a):
    w1.append(int(input('Podaj '+str(i+1)+' wartosc do wektora w1: ')))
print('-------------')
for i in range(a):
    w2.append(int(input('Podaj '+str(i+1)+' wartosc do wektora w2: ')))
print('Iloczyn skalarny '+str(w1)+' i '+str(w2)+' to '+str(funkcja(w1,w2)))
