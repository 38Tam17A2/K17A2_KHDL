M = int(input("Nhập vào năm dương lich: "))
Can = {"Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỷ"}
Chi = {"Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"}
if M % 10 & M % 12:
    print("Năm",M,"lịch âm là năm",M%10,M%12)
else:
    print("Năm nhập vào không hợp lệ")

    