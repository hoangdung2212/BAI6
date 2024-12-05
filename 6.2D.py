print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

# Ví dụ sử dụng class Hinhchunhat
chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
hinhchunhat = Hinhchunhat(chieu_dai, chieu_rong)
print(f"Diện tích của hình chữ nhật là: {hinhchunhat.dien_tich()}")

