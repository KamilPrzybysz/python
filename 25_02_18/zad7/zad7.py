def funkcja(w1,w2):
    iloczyn=0
    for i in range(1,4):
        iloczyn=iloczyn+(w1[i]*w2[i])
    return iloczyn

wektor1=[1,2,3,4]
wektor2=[5,6,7,8]
print funkcja(wektor1, wektor2)
