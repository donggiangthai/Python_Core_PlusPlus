""" BÀI TẬP VỀ NHÀ BUỔI 07 - Function:

Bài 01: Viết hàm
        def max_min(*numbers)
    trả lại cả giá trị max, min của nhiều số được truyền vào

Bài 02: Viết hàm
        def reverse_string(str)
    trả lại chuỗi đảo ngược của chuỗi str

Bài 03: Viết hàm
        def is_perfect(n)
    để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
    Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi

Bài 04: Viết hàm
        def is_prime(n)
    để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False

Bài 05: Viết hàm
        def count_upper_lower(str)
    trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str

Bài 06: Viết hàm
        def is_pangram(str, alphabet)
    đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
    Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần

Bài 07: Viết hàm
        def create_matrix(n, m)
    xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j

Bài 08: Viết hàm
        def body_mass_index(m, h)
    để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
      Viết hàm
        def bmi_information(m, h)
    để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h

Bài 09: Viết hàm
        def change_upper_lower(str)
    chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str

Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
        Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)

Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
            F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
    Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
        + Hàm Đệ quy
        + Hàm Không đệ quy

Bài 12: Viết hàm
        def find_x(a_list, x)
    trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1
"""


# Bài 01: Viết hàm
#         def max_min(*numbers)
#     trả lại cả giá trị max, min của nhiều số được truyền vào
def max_min(*numbers):
    """Use max and min function to
    return the value max or min of entry list named numbers."""
    print(f"Max of numbers is {max(numbers)}\nMin of numbers is {min(numbers)}")


# Bài 02: Viết hàm
#         def reverse_string(str)
#     trả lại chuỗi đảo ngược của chuỗi str
def reverse_string(string):
    """Use slicing to make a reverse string."""
    s = string[::-1]
    print(s)


# Bài 03: Viết hàm
#         def is_perfect(n)
#     để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
#     Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi
def is_perfect(n):
    _sum = 0
    for i in range(1, n):
        if n % i == 0:
            _sum += i
    if _sum == n:
        return True
    return False


# Bài 04: Viết hàm
#         def is_prime(n)
#     để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


# Bài 05: Viết hàm
#         def count_upper_lower(str)
#     trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
def count_upper_lower(string):
    count_upper = 0
    count_lower = 0
    for i in string:
        if 65 <= ord(i) <= 90:
            count_upper += 1
        elif 97 <= ord(i) <= 122:
            count_lower += 1
    print(f"Upper numbers is {count_upper}\nLower numbers is {count_lower}")


# Bài 06: Viết hàm
#         def is_pangram(str, alphabet)
#     đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
#     Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần
def is_pangram(string, alphabet):
    if alphabet is not None:
        for i in string:
            if i in alphabet:
                alphabet.remove(i)
                if not alphabet:
                    return True
        return False


# Bài 07: Viết hàm
#         def create_matrix(n, m)
#     xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j
def create_matrix(n, m):
    """List comprehension"""
    a = [[i * j for j in range(1, m + 1)] for i in range(1, n + 1)]
    print(a)


# Bài 08: Viết hàm
#         def body_mass_index(m, h)
#     để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
#       Viết hàm
#         def bmi_information(m, h)
#     để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
def body_mass_index(m, h):
    """Tính chỉ số BMI"""
    bmi = m / (h * 2)
    return bmi


def bmi_information(m, h):
    """Phân loại gầy béo dựa vào bmi
    Dựa trên IDI & WPRO áp dụng cho người Châu Á."""
    bmi = body_mass_index(m, h)
    classification_table = {
        18.5: "Bình thường",
        23: "Tiền béo phì",
        25: "Béo phì độ I",
        30: "Béo phì độ II"
    }
    if bmi < 23:
        print(f"BMI = {bmi:.2f} - {classification_table.get(18.5)}")
    elif 23 <= bmi < 25:
        print(f"BMI = {bmi:.2f} - Thừa cân - {classification_table.get(23)}")
    elif 25 <= bmi < 30:
        print(f"BMI = {bmi:.2f} - Thừa cân - {classification_table.get(25)}")
    else:
        print(f"BMI = {bmi:.2f} - Thừa cân - {classification_table.get(30)}")


# Bài 09: Viết hàm
#         def change_upper_lower(str)
#     chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
def change_upper_lower(string):
    s = string[:]
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
            s = s.replace(s[i], chr(ord(s[i]) + 32))
        elif 97 <= ord(s[i]) <= 122:
            s = s.replace(s[i], chr(ord(s[i]) - 32))
    print(f"Change {string} to {s}")


# Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
#         Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
def count_odd(n):
    if n <= 1:
        return 1
    else:
        return ((n % 10) % 2) + count_odd((n // 10))


# Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
#             F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
#     Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
#         + Hàm Đệ quy
#         + Hàm Không đệ quy
def recursive_tribo(n):
    if n <= 2:
        return 1
    elif n == 3:
        return 2
    else:
        return recursive_tribo(n - 1) + recursive_tribo(n - 2) + recursive_tribo(n - 3)


def tribonacci(n):
    one = 1
    two = 1
    three = 2
    tribo = 0
    if n <= 2:
        return one
    elif n == 3:
        return three
    else:
        for i in range(4, n + 1):
            tribo = one + two + three
            one, two, three = two, three, tribo
        return tribo


# Bài 12: Viết hàm
#         def find_x(a_list, x)
#     trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1
def find_x(a_list, x):
    position = []
    for i in range(len(a_list)):
        if a_list[i] == x:
            position.append(i)
    return position
