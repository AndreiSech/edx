greeting = "Hello, "
name = input("Name: ")
print(greeting + name)
print(f"Nice to meet you {name}")

n = int(input("Number: "))

if n > 0:
    print(f"number {n} is nositive")
elif n == 0:
    print(f"number is EQUALS 0")
else:
    print(f"number {n} is negative")
