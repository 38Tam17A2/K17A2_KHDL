x=float(input("Nhập một số: "))
n=float(input("Nhập một số tiếp theo: "))
S=lambda x, n: (((x**2)+x+1)**n)+(((x**2)+x-1)**n)
print("S=",S(x,n))