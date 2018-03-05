def funkcja(liczba):
	b=liczba**2
	return(str(b))


a=int(input('Podaj liczbe: '))
print('Zwykla funkcja: ')
print(str(funkcja(a)))
print('Lambda: ')
flambda= lambda a: a**2
print(str(flambda(a)))

