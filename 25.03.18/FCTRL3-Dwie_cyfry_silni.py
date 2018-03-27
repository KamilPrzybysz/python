def funkcja(dd):
	n=[]
	for i in range(d-1):
		n.append(int(input()))
		if(n[i]<0 or n[i]>1000000000):
        		exit()

	else:
		for j in range(d-1):
			wynik=1
			dziesiec=0
			jednosc=0
			if(n[j]<=1):
				wynik=1
				dziesiec=0
				jednosc=1
				print(str(dziesiec))
				print((jednosc))
			else:
				for x in range(n[j]):
					wynik=str(n[j]*wynik)
				dziesiec=wynik[len(wynik)-2]
				jednosc=wynik[len(wynik)-2]
				return dziesiec
				return jednosc


d=int(input())
if(d<1 or d>30):
	exit()
n=int(input())
if(n<0 or n>1000000000):
	exit()

print(funkcja(d))
