# QUESTİON1

import math


def function1(n):
    double = lambda a: (float(n + 1) - 3) / math.pow(float(n + 1), 2)
    total = 0
    for i in range(n):
        total += double(n)
    return total


result = 1

# QUESTİON2
def function2(n):
    global r

    r *= ((float(n) / (float(n) + 2)) - 10)

    if n > 1:
        function2(n - 1)


num = int(input("Please enter a number to calculate : "))
print(function1(num))

num = int(input("Please enter a second number to calculate :  "))
function2(num)
print(r)
