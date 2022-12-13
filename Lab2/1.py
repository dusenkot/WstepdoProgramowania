#Zadanie 1 (1.py) Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i obwód
#oraz wyświetla wyniki na ekranie.

a = int(input("Wprowadz wiek: "))
if a < 4 :
    cena= 0
elif a >= 4 <= 18:
    cena= 10
else:
    cena= 20
print(f"Cena biletu:{cena}zl")

