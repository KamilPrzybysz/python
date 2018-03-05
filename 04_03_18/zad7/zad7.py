def funkcja(xyz):
        slownik={0:'zero' , 1:'jeden ', 2:'dwa ', 3:'trzy ', 4:'cztery ', 5:'piec ', 6:'szesc ', 7:'siedem', 8:'osiem',9:'dziewiec'}
        a=xyz
        b=[]
        i=0
        while(xyz!=0):
                a=xyz%10
                xyz=xyz/10
                b.append(str(slownik[a]))
        return(str(b))

liczba=int(input('Podaj liczbe: '))
print(str(funkcja(liczba)))

