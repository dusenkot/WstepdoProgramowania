def dodawanie(a,b):
    return a+b

def odejmowanie(a,b):
    return a-b
def mnozenie(a,b):
    return a*b
def dzielenie(a,b):
    if b==0:
        return
    else:
        return a/b
kalkulator={"+":dodawanie,"-":odejmowanie,"*":mnozenie,"/":dzielenie()}
c=float(input("a"))
v=float(input("b"))

dziełenie=input("podaj dzialanie")

print(kalkulator[dziełenie](c,v))