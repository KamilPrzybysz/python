def funkcja(aa):
	for i in range(aa):
		wynik=[]
		liczby=input()
		liczby=liczby.split()
		wynik.append((2*(int(liczby[0])*(int(liczby[1]))))/(int(liczby[0])+(int(liczby[1]))))
		print(wynik[i])

	return exit()


a=int(input())
print(funkcja(a))
