def funkcja(w1,w2):
	data=[00,00,0000]
	for i in range(1,3):
		data[i]=w2[i]-w1[i]
	return data

data1=[20,9,1997]
data2=[1,3,2018]
print funkcja(data1,data2)
