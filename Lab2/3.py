try:
    a = float(input("Podaj argument 1"))
except:
    print("Podana wartosc nie jest liczba")
    exit()

try:
    b = float(input("Podaj argument 2"))
except:
    print("Podana wartosc nie jest liczba")
    exit()
print("""Jaka operacje chcesz wykonac?5
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
""")
c = int(input("Podaj numer operacji "))
if c == 1:
    print("Wynik wynosi ", a + b)
elif c == 2:
    print("Wynik wynosi ", a - b)
elif c == 3:
    print("Wynik wynosi ", a * b)
elif c == 4:
    if b == 0:
        print("Nie mozna dzielic na prszez 0")
        exit()
    print("Wynik wynosi ", a / b)
elif c == 5:
    print("Wynik wynosi ", a ** b)
else:
    print("Brak operacji z podanym numerem")
