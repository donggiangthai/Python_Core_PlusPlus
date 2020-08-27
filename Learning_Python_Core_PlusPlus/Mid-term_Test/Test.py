"""
Bài 1:
1. Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bàn phím.
2. Viết chương trình nhập vào một số nguyên dương, tính tổng các chữ số của nó.
3. Viết hàm đếm số lần xuất hiện các ký tự trong một String.
Bài 2: Xây dựng chương trình cho phép người dùng nhập vào số kWh điện tiêu thụ rồi tính ra số tiền cần trả?
Bài 3: Viết chương trình cho phép nhập vào số nguyên N, đếm số lượng các số nguyên tố nhỏ hơn N.
"""


# Bài 1:
# 1. Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bàn phím.
# 2. Viết chương trình nhập vào một số nguyên dương, tính tổng các chữ số của nó.
# 3. Viết hàm đếm số lần xuất hiện các ký tự trong một String.
def ex_01():
    print("1. Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bàn phím.")
    s = input("Nhập chuỗi:\n")
    print(f"Ký tự lớn nhất là: {max(s)}\nKý tự nhỏ nhất là: {min(s)}")
    print("2. Viết chương trình nhập vào một số nguyên dương, tính tổng các chữ số của nó.")
    a = input("Nhập số nguyên dương: ")
    list1 = list(a)
    list2 = [int(i) for i in list1]
    print(f"Tổng các chữ số của {a} là: {sum(list2)}")
    print("3. Viết hàm đếm số lần xuất hiện các ký tự trong một String.")
    s = input("Nhập chuỗi:\n")
    a = list(s)
    b = set(a)
    my_dict = {}.fromkeys(a)
    for i in b:
        my_dict.update({i: a.count(i)})
    print(my_dict)


# Bài 2: Xây dựng chương trình cho phép người dùng nhập vào số kWh điện tiêu thụ rồi tính ra số tiền cần trả?
def ex_02():
    print("Xây dựng chương trình cho phép người dùng nhập vào số kWh điện tiêu thụ rồi tính ra số tiền cần trả?")
    a = float(input("Nhập số điện cần tính: "))
    _sum = 0
    while a > 0:
        if a > 300:
            _sum += (a - 300) * 3000
            a -= (a - 300)
        elif 100 < a <= 300:
            _sum += (a - 100) * 2000
            a -= (a - 100)
        elif a <= 100:
            _sum += a * 1500
            a = 0
    print(f"Tổng số tiền điện cần trả là: {_sum}VNĐ")


# Bài 3: Viết chương trình cho phép nhập vào số nguyên N, đếm số lượng các số nguyên tố nhỏ hơn N.
def ex_03():
    import math
    print("Viết chương trình cho phép nhập vào số nguyên N, đếm số lượng các số nguyên tố nhỏ hơn N.")
    a = int(input("Nhập số nguyên N: "))
    count = 0

    def checksnt(n):
        if n < 2:
            return False
        for i in range(2, (int(math.sqrt(n)) + 1)):
            if n % i == 0:
                return False
        return True

    if a <= 2:
        print(f"Không tồn tại số nguyên tố nhỏ hơn N.")
        return
    list1 = []
    for i in range(2, a):
        if checksnt(i):
            list1.append(i)
    print(f"Số lượng các số nguyên tố nhỏ hơn N là: {len(list1)}")
    print(f"Các số nguyên tố nhỏ hơn N:\n{list1}")
