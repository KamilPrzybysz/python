def funkcja(a):
    licz=1
    while a/10!=0:
        a=a/10
        licz=licz+1
    return licz


liczba=input("Podaj liczbe: ")
print funkcja(liczba)
