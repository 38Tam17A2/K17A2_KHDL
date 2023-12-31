def process_tuple():
    my_tuple=('red','green','yellow','blue','black','white','pink','orange','red','blue')
    n=int(input("Nhập index dương:"))
    m=int(input("Nhập index âm:"))
    print("Tuple:",my_tuple)
    if 0<=n<10:
        print("Giá trị của phần tử có index dương đã nhập: ",my_tuple[n])
    else:
        print("index dương không hợp lệ!!!")
    if -10<=m<0:
        print("Giá trị của phần tử có index âm đã nhập: ",my_tuple[m])
    else:
        print("index âm không hợp lệ!!!")
    s_find=input("Nhập chuỗi cần tìm:")
    count=my_tuple.count(s_find)
    print("Số lần xuất hiện của",s_find,"trong tuple:",count)
process_tuple()
        
        