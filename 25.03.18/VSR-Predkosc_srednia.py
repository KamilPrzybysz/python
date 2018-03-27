def funkcja(tt):
	wynik=[]
	for i in range(tt):
		liczby=input()
		liczby=liczby.split()
		if(int(liczby[0])<=1 or int(liczby[1])>=10000):
			return exit()
		wynik.append((2*(int(liczby[0])*(int(liczby[1]))))/(int(liczby[0])+(int(liczby[1]))))
	for i in range(tt):
		print(int(wynik[i]))
	return exit()


t=int(input())
if(t<=1 or t>=10000):
	exit()
print(funkcja(t))
