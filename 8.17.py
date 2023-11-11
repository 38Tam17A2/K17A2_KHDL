a=int(input("Nhap so a: "))
b=int(input("Nhap so b: "))
x,y=a,b
while a != b:
    if a > b:a = a-b
    else : b = b-a
print("Boi chung nho nhat cua", a,"va", b,"la",a*b//x)
    