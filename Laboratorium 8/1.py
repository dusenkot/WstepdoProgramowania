#Zadanie 1. Napisz funkcję find(), która w liście sprawdza czy występuje podana wartość. Lista i wartość są
#parametrami funkcji. Funkcja ma zwracać listę indeksów, pod którymi wystąpiła wartość. Nie wolno korzystać z
#operatora in w celu sprawdzenia czy wartość występuje w liście

def find(lista,wartosc):
    lista1=[]
    for i in range(len(lista)):
        if  lista[i]==wartosc:
            lista1.append(i)
    return (lista1)
print(find([1,8,5,42],7))
print(find("samochod","a"))