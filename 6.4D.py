print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
class RomanToInt:
    def __init__(self):
        self.roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def convert(self, roman):
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = self.roman_numerals[char]
            if value >= prev_value:
                total += value
            else:
                total -= value
            prev_value = value
        return total

# Ví dụ sử dụng class RomanToInt
roman_number = 'XIV'
converter = RomanToInt()
result = converter.convert(roman_number)
print(f"Số nguyên của {roman_number} là: {result}")
