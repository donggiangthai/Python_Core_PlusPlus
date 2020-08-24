""" BÀI TẬP VỀ NHÀ BUỔI 05 - Tuple:

Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
    Sau đó, unpack các phần tử trong một tuple.

Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple

Bài 02: Viết chương trình đảo ngược một tuple.

Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.

Bài 04: Cho 1 list chứa các tuple không rỗng.
    Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
    Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]

Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.

Bài 06: Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple.

Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.

Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.

Bài 09: Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.

Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
    Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.

Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
"""


# Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
#     Sau đó, unpack các phần tử trong một tuple.
def ex_00():
    my_tuple = 'string', 0, 0.1,
    a, b, c = my_tuple


# Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple.
def ex_01():
    a = 'string', 0, 0.1,
    print(f"Tuple to List: {a} to {list(a)}")
    my_tuple = tuple(a)
    print(f"List to Tuple: {list(a)} to {a}")


# Bài 02: Viết chương trình đảo ngược một tuple.
def ex_02():
    my_tuple = (1, 2, 3, 4, 5)
    my_tuple = my_tuple[::-1]
    print(my_tuple)


# Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.
def ex_03():
    my_list = [1, 2, 3, 4, (1, 2, 3), 5]
    count = 0
    for i in my_list:
        if type(i) == tuple:
            break
        count += 1
    print(f"Number of element in list befor tuple is: {count}")


# Bài 04: Cho 1 list chứa các tuple không rỗng.
#     Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
def ex_04():
    a = [(2, 1, 5), (4, 1, 1), (0, 1, 0)]
    my_list = a[:]
    for i in range(len(my_list)):
        my_list[i] = my_list[i][::-1]
    my_list.sort()
    for i in range(len(my_list)):
        my_list[i] = my_list[i][::-1]
    print(my_list)


# Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.
def ex_05():
    a = [(2, 5, 1), (4, 2, 1), (0, 3, 1)]
    b = []
    for i in a:
        b.append(i[1])
    b.sort()
    for i in a:
        if i[1] == b[0]:
            print(f"Tuple satisfy is: {i}")


# Bài 06: Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple.
def ex_06():
    my_tuple = (1, 2, 3, 'string', 0, 9, [1, 2, 3], 1, 1, 1)
    print(f"The fourth element {my_tuple[3]}, the fourth element reverse {my_tuple[-4]}")


# Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
def ex_07():
    tuple_01 = (1, 2, 3)
    tuple_02 = (3, 4, 5)
    a = []
    for i in tuple_01:
        for j in tuple_02:
            if i == j:
                a.append(i)
    print(f"Two tuple have common element: {a}")


# Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
def ex_08():
    tuple_01 = (1, 1, 1)
    check = True
    for i in range(1, len(tuple_01)):
        if tuple_01[i] != tuple_01[i - 1]:
            print(f"All element in tuple are not the same.")
            check = False
            break
    if check:
        print(f"All element in tuple are the same.")


# Bài 09: Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.
def ex_09():
    my_tuple = (1.5, 0.3, 2.6)
    print(f"The sum of the tuple: {sum(my_tuple)}\nMax element in tuple: {max(my_tuple)}")


# Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
#     Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
def ex_10():
    my_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
    a = []
    for i in my_list:
        b = list(i.split("."))
        a.append((b[-1], b[1]))
    # Plan A: Use dictionary
    print(f"Use dictionary")
    my_dict = dict(a)
    for i in my_list:
        for j in my_dict:
            if my_dict.get(j) in i:
                print(f"Website {i} have a suffix is {j}")
    # Plan B: Use Tuple
    print(f"Use Tuple")
    for i in my_list:
        for j in a:
            if j[1] in i:
                print(f"Website {i} have a suffix is {j[0]}")


# Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
def ex_11():
    s = "Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím."
    a = list(s.split())
    word = ''
    for i in a:
        if len(i) > len(word):
            word = i
    print(word)