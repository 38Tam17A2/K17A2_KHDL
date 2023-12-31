x=float(input("Nhập một số: "))
n=float(input("Nhập một số tiếp theo: "))
S=lambda x, n: ((x**2)+1)**n
print("S=",S(x,n))