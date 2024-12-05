print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Ví dụ sử dụng class Circle
radius = float(input("Nhập bán kính của hình tròn: "))
circle = Circle(radius)
print(f"Diện tích của hình tròn là: {circle.area()}")

