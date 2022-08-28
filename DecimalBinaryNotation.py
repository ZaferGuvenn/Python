liste=[]
liste2=[]
sayi=500#your number here...
print("Number= "+str(sayi))
sonuc=1
i=0
kalan=0
while(sayi>1):
  kalan=sayi%2
  sayi=int(sayi/2)  
  liste.append(kalan)
  if(kalan==1):
    j=i
    sonuc=1
    if(j==0):
      sonuc=1
    while(j>0):
      sonuc=sonuc*2
      j=j-1
    liste2.append(sonuc)
    
  else:
    liste2.append(0)
  i=i+1

j=i
sonuc=1
while(j>0):
  sonuc=sonuc*2
  j=j-1
  
liste2.append(sonuc)

liste.append(1)
liste.reverse()
liste2.reverse()

toplam=0
toplamli=""
binary=""
for i in liste2:
  toplamli=toplamli+"+"+str(i)
  toplam=toplam+i
for i in liste:
  binary=binary+" "+str(i)
  
print("Binary representation= "+binary)
print("Decimal notation= "+toplamli+"= "+str(toplam))
