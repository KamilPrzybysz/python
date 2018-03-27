def funkcja(aa, bb, cc):
	wynik=aa+bb+cc
	return wynik

a=int(input())
if(a>100):
	exit()
b=int(input())
if(b>100):
        exit()

c=int(input())
if(c>100):
        exit()

print(funkcja(a,b,c))
