nazwa=open('muzyka.mp3','rb')
print(nazwa.name)
print(nazwa.mode)

if(not nazwa.close()):
    print('Plik otwarty')
else:
    print('Plik zamkniety')
nazwa.close()
if(nazwa.close()):
    print('Plik otwarty')
else:
    print('Plik zamkniety')
