def funkcja():
	liczby=input()
	liczby=liczby.split()
	a=int(liczby[0])
	b=int(liczby[1])
	c=int(liczby[2])
	d=int(liczby[3])
	wynik=a*b+c*d
	print(wynik)
	return exit()

print(funkcja())
