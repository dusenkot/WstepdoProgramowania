import random
import math
#punkty=[]
#for i in range(15):
 #   a= random.uniform(0, 50)
  #  b=round(a,2)
   # punkty.append(b)

#print(punkty)
punkty=[round(random.uniform(0,50),2)for i in range(15)]

print(max(punkty),min(punkty))
print(punkty)
a=float(input("Prosze podać liczbe punktów: "))
if a in punkty:
    print(punkty.index(a))
else:
    print("Brak wartości w liście")

b=(punkty)/len(punkty)
b=round(b,2)
print(b)
list1 = []
list2 = []
for i in punkty:
    if i < b:
        list1.append(i)
print(len(list1))
print(list1)

list2=[i for i in punkty if i > b ]
print(len(list2))
print(list2)
