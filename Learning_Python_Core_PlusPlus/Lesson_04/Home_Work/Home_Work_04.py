""" BÀI TẬP VỀ NHÀ BUỔI 04 - List:

Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.

Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list.

Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.

Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.

Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.

Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
        Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.

Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau

Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.

Bài 08: Cho list các số nguyên dương A.
        Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.

Bài 09: Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).

Bài 10:
Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
       Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
Input: A - mảng chứa id của mỗi bài hát
Output: Độ dài cần tìm
Example:
    Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
    => Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5]
"""


def ex_00():
    import random
    print("Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.")
    my_list = list(input("Enter the element of list split by comma:\n").split(","))
    a = []
    while len(a) < 5:
        i = random.randint(0, len(my_list))
        if my_list[i] not in a:
            a.append(my_list[i])
    print(f"New list is: {a}")


def ex_01():
    print("Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list.")
    my_list = list(input("Enter the element of list split by comma:\n").split(","))
    sum_list = 0
    multi_list = 1
    for i in my_list:
        sum_list += i
        multi_list *= i
    print(f"Tổng các phần tử trong list là: {sum_list}")
    print(f"Tích các phần tử trong list là: {multi_list}")


def ex_02():
    print("Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.")
    my_list = list(input("Enter the element of list split by comma:\n").split(","))
    print(f"Số lớn nhất trong list là: {max(my_list)}")
    print(f"Số nhỏ nhất trong list là: {min(my_list)}")


def ex_03():
    print("Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.")
    my_list = list(input("Enter the element of list split by comma:\n").split(","))
    s = input("Enter the string need concatenate:\n")
    my_list.append(s)
    print(f"New list is: {my_list}")


def ex_04():
    print("Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.")
    my_list = list(input("Enter the element of list split by comma:\n").split(","))
    m = int(input("Enter the length of first list:\n"))
    print(f"List after split is:\n The first: {my_list[:m]}\n The second: {my_list[m:]}")


def ex_05():
    print("Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list. Nếu có nhiều phần "
          "tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.")
    my_list = list(input("Enter the element of list split by comma:\n").split(","))
    element_max_count = 0
    max_count = 0
    for i in my_list:
        if my_list.count(i) > max_count:
            element_max_count = i
            max_count = my_list.count(i)
    print(f"The most appears element is: {element_max_count} with {max_count} appearances")


def ex_06():
    print("""Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau""")
    my_list = list(input("Enter the element of list split by comma:\n").split(","))
    count = 0
    for i in my_list:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    print(f"Number of string satisfy the conditions is: {count}")


def ex_07():
    print("Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.")
    list_01 = list(input("Enter the element of first list split by comma:\n").split(","))
    list_02 = list(input("Enter the element of second list split by comma:\n").split(","))
    a = False
    for i in list_01:
        if i in list_02:
            a = True
            print(f"Two list have a common part is: {i}")
    if not a:
        print(f"Two list does not have any common part.")


def ex_08():
    print("""Bài 08: Cho list các số nguyên dương A.
        Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.""")
    my_list = list(input("Enter the element of list split by comma:\n").split(","))
    count = 0
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            if my_list[i] > my_list[j]:
                count += 1
    print(f"Number of nested satisfy the conditions is: {count}")


def ex_09():
    print("Bài 09: Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).")
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            _sum = 0
            for k in range(3):
                _sum += (a[i][k] * b[k][j])
            c[i][j] = _sum
    print(f"Matrix a = {a}\nMatrix b = {b}\nMatrix c = {c} = Matrix a * Matrix b")


def ex_10():
    print("""Bài 10:
Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
       Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp 
       trong đó không có bài hát nào được lặp lại.
Input: A - mảng chứa id của mỗi bài hát
Output: Độ dài cần tìm
Example:
    Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
    Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5]""")
    my_list = list(input("Enter list of song split by comma:\n").split(","))
    a = []
    for i in my_list:
        if i not in a:
            a.append(i)
    print(f"Output = {len(a)}. Sequence of songs in a row: {a}")

