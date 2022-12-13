#Zadanie 3 (3.py):
#• Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
#• Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
#• Dla osób powyżej 18 roku życia bilet kosztuje 20zł.
#Przykład: Wprowadź wiek klienta: 5
#Cena biletu: 10zł
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
