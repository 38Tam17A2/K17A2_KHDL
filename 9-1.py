def sign(x):
    if x<0:
        return -1
    elif x>0:
        return 1
    else:
        return 0
a=int(input("Nhập một số:"))
print(sign(a))