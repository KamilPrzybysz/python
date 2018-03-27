def funkcja(aa):
	sumy=[]
	for i in range(aa):
		lista=[]
		wynik=0
		b=int(input())
		lista=input()
		lista=lista.split()
		for j in range(b):
			wynik=int(lista[j])+int(wynik)
		sumy.append(str(wynik))
	print('\n'.join(sumy))
	return exit()

a=int(input())
if(a<0 or a>100):
	exit()
print(funkcja(a))
