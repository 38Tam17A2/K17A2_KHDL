import math
r=float(input("Nhập vào bán kính của hình tròn: "))
a=float(input("Nhập vào chiều dài của HCN: "))
b=float(input("Nhập vào chiều rộng của HCN: "))
S=lambda r: math.pi*(r**2)
print("S=",S(r))
C=lambda r: r*2*3.14
print("C=",C(r))
P=lambda a, b: (a+b)*2
print("P=",P(a,b))
s=lambda a, b: a*b
print("s=",s(a,b))