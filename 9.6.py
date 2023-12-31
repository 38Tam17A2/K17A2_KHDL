x=float(input("Nhập vào một số: "))
if x < 2:
    print("False")
elif x == 2:
    print("True")
elif (x % 2) == 0:
    print("False")
else:
    for i in range(3, x, 2):
        if (x % i) == 0:
            print("False")
