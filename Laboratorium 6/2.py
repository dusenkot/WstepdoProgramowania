def oblicz(liczba1 ,liczba2):
    suma=liczba1+liczba2
    róznica=liczba1-liczba2
    return suma,róznica


print(oblicz(22,13))

x, y = oblicz(4.14,8.4)
print(f"Suma = {x},Roznica = {y}")