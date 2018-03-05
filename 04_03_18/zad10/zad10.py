lista=[]
for i in range(4):
	lista.append(int(input('Podaj liczbe: ')))
a=0
while(a<2 and a>5):
	a=int(input('Podaj liczbe miedzy 2, a 5: '))
b=0
flambda(lambda b, lista, a: b=b+lista[i], range(a))
print('Suma '+str(a)+' liczb z listy '+str(lista)+' to: '+str(b))
