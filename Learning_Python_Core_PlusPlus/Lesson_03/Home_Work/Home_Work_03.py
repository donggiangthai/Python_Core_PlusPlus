""" BÀI TẬP VỀ NHÀ BUỔI 03 - String

Bài 01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.

Bài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.

Bài 03: Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.

Bài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.

Bài 05: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.

Bài 06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.

"""


def ex_01():
    print("Bài 01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.")
    s = input("Enter the string that you want to change: ")
    s = s.replace(s[0], "$")
    print("New string is:", s)


def ex_02():
    print("Bài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn "
          "phím.")
    s = input("Enter the string that you want to change: ")
    m = int(input("Enter position m that you want to delete on string: "))
    while m < 0:
        print("Please just enter m with non-negative numbers.")
        m = int(input("Enter m again: "))
    s = s.replace(s[(m - 1)], "", 1)
    print("New string is:", s)


def ex_03():
    print("Bài 03: Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.")
    s = input("Enter the string that you want to change: ")
    a = s[0::2]
    print("New string is:", a)


def ex_04():
    print("Bài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, "
          "nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.")
    s = input("Enter the string that you want to change: ")
    a = s[0:2] + s[len(s) - 2:len(s)]
    print("New string is:", a)


def ex_05():
    print("Bài 05: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.")
    s = input("Enter the string: ")
    print("Max character on string is {} which have code {}".format(max(s), ord(max(s))))
    print("Min character on string is {} which have code {}".format(min(s), ord(min(s))))


def ex_06():
    print("Bài 06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong "
          "một chuỗi.")
    s = input("Enter the string that you want to change: ")
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
            s = s.replace(s[i], chr(ord(s[i])+32))
        elif 97 <= ord(s[i]) <= 122:
            s = s.replace(s[i], chr(ord(s[i])-32))
    print("New string is:", s)



