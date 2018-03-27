def funkcja(aa):
        liczby=[]
        for i in range(aa):
            liczby.append(int(input()))
        for i in range(aa):
            if(int(liczby[i])>10000 or liczby[i]>=2):
                for x in range(2, liczby[i]):
                    if(liczby[i]%x==0):
                        print("NIE")
                        break
                else:
                     print("TAK")
            else:
                print("NIE")
        return exit()
a=int(input())
if(a>=100000):
        exit()
print(funkcja(a))
