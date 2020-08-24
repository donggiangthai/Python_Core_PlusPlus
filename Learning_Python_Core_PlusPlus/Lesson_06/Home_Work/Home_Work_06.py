""" BÀI TẬP VỀ NHÀ BUỔI 06 - DICTIONARY:

Bài 00: Viết chương trình tính tích value của các phần tử trong một dict

Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict

Bài 02: Viết chương trình sắp xếp các phần tử của dict theo chiều tăng dần của key

Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict

Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict

Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
        Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict

Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict

Bài 07: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
Ví dụ:
    dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
    keys = ["name", "salary"]
    Output: {'name': 'Kelly', 'salary': 8000}

Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict

Bài 09: Viết hàm đếm số lần xuất hiện các ký tự trong một String
Ví dụ:
    Input: ‘Stringings’
    Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}

Bài 10: Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản

Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
Ví dụ:
    Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    Output: {'item1': 1150, 'item2': 300}

"""


# Bài 00: Viết chương trình tính tích value của các phần tử trong một dict.
def ex_00():
    my_dict = {
        1: 10,
        2: 20,
        3: 30
    }
    area = 1
    for i in my_dict.values():
        area *= i
    print(area)


# Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict.
def ex_01():
    my_dict = {
        1: 10,
        2: 20,
        3: 30
    }
    print(f"Max value in dict: {max(my_dict.values())}\nMin value in dict: {min(my_dict.values())}")


# Bài 02: Viết chương trình sắp xếp các phần tử của dict theo chiều tăng dần của key.
def ex_02():
    my_dict = {
        1: 20,
        2: 30,
        3: 10,
        0: 100,
    }
    a = sorted(my_dict)
    new_dict = {}.fromkeys(a)
    for i in a:
        new_dict.update({i: my_dict[i]})
    print(new_dict)


# Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict.
def ex_03():
    my_dict = {
        1: 20,
        2: 30,
        3: 10,
        0: 10,
    }
    a = sorted(set(my_dict.values()))
    print(f"{my_dict.values()}\nDict which no duplicated values: {a}")


# Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict.
def ex_04():
    my_dict = {
        1: 20,
        2: 30,
        3: 10,
        0: 10,
    }
    a = sorted(my_dict, reverse=True)
    b = a[:3]
    for i in b:
        print(f"({i} : {my_dict.get(i)})")


# Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
#         Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict.
def ex_05():
    sub_dict = {
        1: 10,
        2: 20,
        3: 30,
        4: 40,
        5: 50,
        6: 60
    }
    my_dict = {}.fromkeys([1, 2, 3, 4], sub_dict)
    for i in my_dict:
        count = 0
        for j in my_dict[i]:
            count += 1
            if count == 5:
                print(f"The fifth element of key '{i}' is:  ({j}, {my_dict.get(i).get(j)})")


# Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict.
def ex_06():
    dicy_01 = {
        1: 10,
        2: 20,
        3: 30,
        4: 40,
        5: 50
    }
    dicy_02 = {
        1: 1,
        2: 20,
        3: 3,
        4: 40,
        5: 5
    }
    for i in dicy_01:
        for j in dicy_02:
            if i == j and dicy_01.get(i) == dicy_02.get(j):
                print(f"Duplicate key, value is: ({j}, {dicy_02.get(j)})")


# Bài 07: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước.
def ex_07():
    sampleDict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    keys = ["name", "salary"]
    new_dict = {}.fromkeys(keys)
    for i in keys:
        new_dict.update({i: sampleDict.get(i)})
    print(new_dict)


# Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict.
def ex_08():
    my_dict = {
        1: 20,
        2: 30,
        3: 10,
        0: 10,
    }
    a = sorted(my_dict.values(), reverse=True)
    b = a[:3]
    for i in range(len(b)):
        print(f"Top {i+1} is: {b[i]}")


# Bài 09: Viết hàm đếm số lần xuất hiện các ký tự trong một String.
def ex_09():
    s = input("Enter the string: ")
    a = list(s)
    for i in range(len(a)):
        if a[i] == ' ':
            a[i] = 'space'
    b = set(a)
    my_dict = {}.fromkeys(a)
    for i in b:
        my_dict.update({i: a.count(i)})
    print(my_dict)


# Bài 10: Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản.
def ex_10():
    text = input("Enter the document:\n")
    a = list(text.split())
    b = set(a)
    my_dict = {}.fromkeys(a)
    for i in b:
        my_dict.update({i: a.count(i)})
    print(my_dict)


# Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
# Ví dụ:
#     Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#     Output: {'item1': 1150, 'item2': 300}
def ex_11():
    a = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    my_dict = dict()
    b = []
    for i in a:
        b.extend(i)
    b = set(b)
    key = ''
    value = ''
    for i in a:
        for j in b:
            if type(i.get(j)) == str:
                key = j
            else:
                value = j
    for i in a:
        if i.get(key) not in my_dict:
            my_dict.update({i.get(key): i.get(value)})
        else:
            a = my_dict.get(i.get(key))
            a += i.get(value)
            my_dict.update({i.get(key): a})
    print(my_dict)

