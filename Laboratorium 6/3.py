x=0
def Zad3(*args):
    print(args)
    for i in args:
        print(i)
    print()

#Zad3(3,31.21,"list",["pies","kot"])
#Zad3(1.2,3,"Małpa")

def max(*args):
    m=args[0]
    for i in args:
        if m < i:
            m=i
    return  m
print(max(9,-4,5,7))