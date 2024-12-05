print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def dien_tich(self):
        return math.pi * self.radius ** 2

    def chu_vi(self):
        return 2 * math.pi * self.radius

# Ví dụ sử dụng class Circle
radius = float(input("Nhập bán kính của hình tròn: "))
circle = Circle(radius)
print(f"Diện tích của hình tròn là: {circle.dien_tich()}")
print(f"Chu vi của hình tròn là: {circle.chu_vi()}")

