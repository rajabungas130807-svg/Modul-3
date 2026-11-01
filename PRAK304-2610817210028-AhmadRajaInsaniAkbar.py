a=int(input())

if a==0 :
    print("nol")
elif a>=1 and a <=9 :
    print ("satuan")
elif a>=10 and a<=19 :
    print ("belasan")
elif a>=20 and a <=99 :
    print ("puluhan")
else :
    print("Anda Menginput Melebihi Limit Bilangan")