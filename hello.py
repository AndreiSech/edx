greeting = "Hello, "
# name = input("Name: ")
name = "Harry"
print(greeting + name)
print(f"Nice to meet you {name}")

sym = name[0]
print(f"you name starts with {sym}")

# array
names = ["Peter", "Joe", "Marie"]
print(names)
print("My name is " + names[0])

names.append("Michael")
names.sort()
print(names)

# set
numbers = set()
numbers.add(1)
numbers.add(3)
numbers.add(7)
numbers.add(6)
numbers.add(3)
numbers.remove(6)
print(numbers)
print(f"The set has {len(numbers)} elements")

# dictionary
teams = { "De Bruyne": "MC", "Salah": "Liverpool"}
teams["Mane"] = "Liverpool"
print(teams["Salah"])

# n = int(input("Number: "))
n = 5

if n > 0:
    print(f"number {n} is nositive")
elif n == 0:
    print(f"number is EQUALS 0")
else:
    print(f"number {n} is negative")


def square(x):
    return x * x


coordinateX = 5.0
coordinateY = 2.2

coordinates = (coordinateX, coordinateY)
sum = 0
for coordinate in coordinates:
    sum += square(coordinate)
distanceSquared = sum
print(sum)

class Point():
    def __init__(self, inputX, inputY):
        self.x = inputX
        self.y = inputY

p = Point(coordinateX, coordinateY)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

f = Flight(3)
people = names
for p in people:
    if f.add_passenger(p):
        print(f"The passengers {p} was added")
    else:
        print(f"No avaliable seats for {p}")

#for i in [0, 1, 2, 3, 4, 5]:
#    print(i)

for i in range(3):
    print(i)

for c in name:
    print(c)
