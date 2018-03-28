def funkcja(tt):
	wynik=[]
	for i in range(tt):
		liczby=input()
		liczby=liczby.split()
		a=int(liczby[0])
		b=int(liczby[1])
		if(a<0 or a>1000000):
			return exit()
		if(b<0 or b>1000000):
                        return exit()
		while True:
			if(a<b):
				b=b-a
			else:
				a=a-b
			if(a==b):
				break
		wynik.append(a)
	for i in range(tt):
		print(int(wynik[i]))
	return exit()






t=int(input())
print(funkcja(t))




