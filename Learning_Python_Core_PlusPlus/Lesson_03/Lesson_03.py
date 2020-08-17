# n, m = int(input("Nhập n:")), int(input("Nhập m:"))
# for i in range(n):
#     for j in range(m):
#         print('*', end=" ")
#     print()

# epsilon = float(input("Enter the value of epsilon:"))
# n = 1
# Sum = 0
# while n <= 1/epsilon:
#     Sum += 1/n
#     n += 1
# print(Sum)

# for i in range(10, 100):
#     if not (i % 2) or not (i % 3) or not (i % 5):
#         continue
#     print(i, end=" ")

s = input()

for i in range(len(s)):
    if s[i] == 'a':
        print(i)
