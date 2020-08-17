# my_list = [1, 2, 3, 4, 5, 6]
#
# my_list_2 = [1, 2, 3, 4, 5, 6]
#
# a = my_list + my_list_2
#
# print(a)

language = ["Python", "C/C++", "C#", "Java"]
keys = ["Language", "Programming"]
print([x+y for x in language for y in keys])
