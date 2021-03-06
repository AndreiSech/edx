import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: cannot divide by 0")
    sys.exit(1)

# print(str(x) + " / " + str(y) + " = " + str(result))

print(f"{x} / {y} = {result}")