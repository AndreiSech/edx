people = [
    {"name": "Aaron", "age" : 28},
    {"name": "Kayn", "age": 32},
    {"name": "Teresa", "age": 45},
    {"name": "Sharon", "age": 18}
]

def f(person):
    return person["age"]

people.sort(key = f)
print(people)

people.sort(key = lambda person: person["name"])
print(people)


