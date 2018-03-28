def funkcja(tt):
	odwrot=[]
	for i in range(tt):
		liczby=input()
		liczby=liczby.split()
		a=len(liczby)
		for i in range(a-1, 0, -1):
			odwrot.append(liczby[i])
		odwrot.append("\n")

	print(' '.join(odwrot))
	return exit()

t=int(input())
if(t>100):
	exit()
print(funkcja(t))
