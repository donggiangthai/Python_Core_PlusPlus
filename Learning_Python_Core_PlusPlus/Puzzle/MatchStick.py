numStick = int(input("The number of stick:"))
# one = 2
# two = 5
# three = 5
# four = 4
# five = 5
# six = 6
# seven = 3
# eight = 7
# nine = 6
# zero = 6

if numStick < 2:
    print("Can't puzzle.")
numMax = 0
if numStick % 2 == 1:
    temp = numStick - 3
    numOfOne = temp // 2
    for i in range(numOfOne):
        numMax += 1 * 10 ** i
    numMax += 7 * 10 ** numOfOne
else:
    numOfOne = numStick // 2
    for i in range(numOfOne):
        numMax += 1 * 10 ** i
print("Max number is:", numMax)
numMin = 0
if numStick < 14:
    if numStick == 13:
        print("Min number is:", numMin + 68)
    elif numStick == 12:
        print("Min number is:", numMin + 28)
    elif numStick == 11:
        print("Min number is:", numMin + 20)
    elif numStick == 10:
        print("Min number is:", numMin + 22)
    elif numStick == 9:
        print("Min number is:", numMin + 18)
    elif numStick == 8:
        print("Min number is:", numMin + 10)
    elif numStick == 7:
        print("Min number is:", numMin + 8)
    elif numStick == 6:
        print("Min number is:", numMin)
    elif numStick == 5:
        print("Min number is:", numMin + 2)
    elif numStick == 4:
        print("Min number is:", numMin + 4)
    elif numStick == 3:
        print("Min number is:", numMin + 7)
    elif numStick == 2:
        print("Min number is:", numMin + 1)
else:
    s = "8"
    n = numStick // 7
    if numStick % 7 == 0:
        print("Min number is:", s * n)
    elif numStick % 7 == 1:
        print("Min number is:", "10" + s * (n-1))
    elif numStick % 7 == 2:
        print("Min number is:", "1" + s * n)
    elif numStick % 7 == 3:
        print("Min number is:", "200" + s * (n-2))
    elif numStick % 7 == 4:
        print("Min number is:", "20" + s * (n-1))
    elif numStick % 7 == 5:
        print("Min number is:", "2" + s * n)
    elif numStick % 7 == 6:
        print("Min number is:", "6" + s * n)


