def funkcja(aa,bb):
    while(bb!=0):
        aa,bb=bb,aa%bb
    return aa



a=int(input('Podaj liczbe a: '))
b=int(input('Podaj liczbe b: '))
print('NWD'+str(a)+' i '+str(b)+' to '+str(funkcja(a,b)))
