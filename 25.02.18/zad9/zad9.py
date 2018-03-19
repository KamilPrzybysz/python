def funkcja(xyz):
	abc=str(xyz)
	a=len(abc)
	for i in range(0, a):
		if abc[i]=="1":
			print "jeden "
		elif abc[i]=="2":
			print "dwa"
		elif abc[i]=="3":
                 	print "trzy"
		elif abc[i]=="4":
                       	print "cztery"
		elif abc[i]=="5":
                       	print "piec"
		elif abc[i]=="6":
                       	print "szesc"
		elif abc[i]=="7":
                       	print "siedem"
		elif abc[i]=="8":
                       	print "osiem"
		elif abc[i]=="9":
                       	print "dziewiec"
		elif abc[i]=="0":
                       	print "zero"
		else:
			print"\n"
	exit()

liczba=input("Podaj liczbe: ")
print funkcja(liczba)


