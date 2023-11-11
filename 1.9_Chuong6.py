#baiap1.9
Lãi_suất_một_năm=float(input("Nhập lãi suất một năm : "))
Số_tiền_gửi=float(input("Nhập số tiền gửi : "))
Số_tháng_gửi=float(input("Nhập số tháng gửi : "))
Tiền_lãi=(Số_tiền_gửi*Số_tháng_gửi)*(Lãi_suất_một_năm/12)
Tổng_tiền_gửi=Số_tiền_gửi+Tiền_lãi
print((Số_tiền_gửi, "*", Số_tháng_gửi), "*", (Lãi_suất_một_năm, "/", 12, "=", Tiền_lãi))
print(Số_tiền_gửi, "+", Tiền_lãi, "=", Tổng_tiền_gửi)
