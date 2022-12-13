#Zadanie 2 (2.py) Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie
#spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu paliwa oraz o szacowanych
#kosztach podróży (cena paliwa 6.5 zł/l).

x= input("wprowadz litere: ")
if len(x)>1 or len(x)==0 :
    print("blad")
    exit()
if "a"<= x <= "z":
    print("litera jest mala ")
elif "A"<= x <="Z":
    print("litera jest duza ")
else:
    print("to nie jest litera")
