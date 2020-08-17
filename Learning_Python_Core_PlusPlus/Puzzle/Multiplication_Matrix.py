import numpy as np
checker = True
n = 0
for i in a:
    if len(i) != len(b):
        checker = False
if checker:
    print(f"Can multiplication matrix a and matrix b!")
    n = len(a)
    p = len(b[0])
    for i in range(len(a[0])):
        for j in range(len(b)):
            _sum = 0
            for k in range(3):
                _sum += (a[i][k] * b[k][j])
            c[i][j] = _sum
    print(f"{a} X {b} = {c}")
else:
    print(f"Can not multiplication matrix a and matrix b!")