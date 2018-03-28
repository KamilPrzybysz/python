def funkcja(tt):
    lista=[]
    for i in range(tt):
        a=int(input())
        wynik=a*a
        lista.append(str(wynik))
    
    print('\n'.join(lista))
    return exit()
    
t=int(input())
if(t<0 or t>500):
    exit()
print(funkcja(t))
