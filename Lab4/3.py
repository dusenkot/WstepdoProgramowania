zwierzeta=[]

c=int(input("Napisze licbze zwierząt"))
for i in range(c):
    x=input('Podaj nazwe zwierząt')
    zwierzeta.append(x)
sorted(zwierzeta)
print(zwierzeta[0],zwierzeta[-3:])
print(len(zwierzeta))