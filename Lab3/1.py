a = int(input())
b = int (input())
if a<b:
    a,b = b,a
while b <= a:
    print(b)
    b=b+1