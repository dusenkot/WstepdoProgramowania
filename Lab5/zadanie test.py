slownik=[]
for i in range(5):
    x=int(input("Wpiszy liczby"))
    if x >= -10 and x <= 10:
            slownik.append(x)
    else:
        print("Error")
print(slownik)