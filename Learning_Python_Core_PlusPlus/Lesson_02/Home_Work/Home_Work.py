"""
    -Lesson 02: List of function:
        +Exercises 1: lesson_02_ex_01
        +Exercises 2: lesson_02_ex_02
        +Exercises 3: lesson_02_ex_03
        +Exercises 4: lesson_02_ex_04
"""


def lesson_02_ex_01():
    print("Exercises 1: Tính nghiệm hệ phương trình bậc 2.")
    a, b, c = float(input("Nhập vào a:")), float(input("Nhập vào b:")), float(input("Nhập vào c:"))
    print("Phương trình nhập vào là: {}x^2 + {}x + {} = 0.".format(a, b, c))
    if a == 0:
        print("Phương trình có nghiệm duy nhất x =", (-c / b))
    else:
        delta = round((b ** 2) - (4 * a * c), 2)
        if delta == 0:
            print("Phương trình có nghiệm thực x =", (-b) / (2 * a))
        elif delta > 0:
            print("Phương trình có hai nghiệm phân biệt:")
            print("x1 =", ((-b) + delta ** (1 / 2)) / (2 * a))
            print("x2 =", ((-b) - delta ** (1 / 2)) / (2 * a))
        else:
            print("Phương trình có 2 nghiệm phức phân biệt:")
            delta = round(abs(delta) ** (1 / 2), 2)
            print("x1 =", complex((-b), delta) / (2 * a))
            print("x2 =", complex((-b), -delta) / (2 * a))
    print("Exercises 1 is Done!")


def lesson_02_ex_02():
    print("Exercises 2: Tính tổng.")

    n, x = int(input("Nhập vào số nguyên dương n:")), float(input("Nhập vào số thực x:"))

    print("Exercises 2.1:")
    S1 = 0
    for n in range(n + 1):
        S1 += x ** n
    print(round(S1, 3))

    print("Exercises 2.2:")
    S2 = 0
    for n in range(n + 1):
        S2 += (-1) ** n * x ** n
    print(round(S2, 3))

    print("Exercises 2.3:")

    def giai_thua_de_quy(i):
        if i == 0:
            return 1
        return i * giai_thua_de_quy(i - 1)

    S3 = 0
    for n in range(n + 1):
        S3 += (x ** n) / giai_thua_de_quy(n)
    print(round(S3, 3))


def lesson_02_ex_03():
    print("Exercises 3: Tính tổng các chữ số của số n.")

    n = int(input("Nhập số nguyên dương n < 1000:"))
    while n > 1000:
        n = int(input("Nhập số nguyên dương n < 1000:"))
    sum_n = 0
    while n > 0:
        sum_n += n % 10
        n = n // 10
    print(sum_n)


def lesson_02_ex_04():
    print("Exercises 4: Xác định tam giác.")

    a, b, c = float(input("Nhập vào số a:")), float(input("Nhập vào số b:")), float(input("Nhập vào số c:"))

    if a + b > c and a + c > b and b + c > a:
        print("a, b, c vừa nhập là độ dài ba cạnh của một tam giác", end=' ')
        if a == b == c:
            print("đều.")
        elif (a == b) or (a == c) or (b == c):
            print("cân.")
        elif (a == b and (a ** 2 + b ** 2) == c ** 2) or (a == c and (a ** 2 + c ** 2) == b ** 2) or (
                c == b and (c ** 2 + b ** 2) == a ** 2):
            print("vuông cân.")
        elif (a ** 2 + b ** 2) == c ** 2 or (a ** 2 + c ** 2) == b ** 2 or (c ** 2 + b ** 2) == a ** 2:
            print("vuông.")
        elif (a ** 2 + b ** 2) < c ** 2 or (a ** 2 + c ** 2) < b ** 2 or (c ** 2 + b ** 2) < a ** 2:
            print("tù.")
    else:
        print("a, b, c vừa nhập không là độ dài ba cạnh của một tam giác")

