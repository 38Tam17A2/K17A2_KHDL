a=int(input("Nhap so a : "))
b=int(input("Nhap so b : "))
while(a*b!=0):
    if a>b:
        a%=b
    else:
        b%=a
print(a+b) 