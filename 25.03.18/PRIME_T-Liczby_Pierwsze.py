def funkcja(aa):
	liczby=[]
	if(a>=10000):
		return exit()
	else:
		for i in range(a):
			liczby.append(int(input()))
		for j in range(a):
			if(liczby[j]>=2):
				for x in range(2, liczby[j]):
					if(liczby[j]%x==0):
						print("NIE")
						break
				else:
					print("TAK")
			else:
				print("NIE")

	return exit()
a=int(input())
print(funkcja(a))
