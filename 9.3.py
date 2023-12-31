x=float(input("Nhập cân nặng(kg): "))
y=float(input("Nhập chiều cao(m): "))
bmi= x/(y*y)
print("Chỉ số BMI của bạn là: ",bmi)
if bmi < 18.5:
    print("Bạn bị thiếu cân nặng!!!")
elif 18.5< bmi <24.99:
    print("Thân hình bạn cân đối!!!")
elif bmi >=25:
    print("Bạn có đôi chút mummim chubby!!!")
else:
    print("Quá tầm kiểm soát!!!")