# Lists

numbers = [10, 20, 30, 40, 50]

numbers.append(60)
numbers.remove(20)

print("List:", numbers)
print("First:", numbers[0])
print("Last:", numbers[-1])
print("Slice:", numbers[1:4])
print("Reversed:", numbers[::-1])


# Tuples

coordinates = (10, 20, 30)

print("Tuple:", coordinates)
print("First:", coordinates[0])
print("Slice:", coordinates[1:])
print("Count:", coordinates.count(20))
print("Index:", coordinates.index(30))


# Sets

numbers = {1, 2, 3, 3, 4}

numbers.add(5)
numbers.remove(2)

print("Set:", numbers)

a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)


# Dictionaries

person = {
    "name": "Alice",
    "age": 25,
    "language": "Python",
}

print("Name:", person["name"])

person["age"] = 26
person["city"] = "Delhi"

print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())

print("Name:", person.get("name"))
print("Country:", person.get("country", "Unknown"))

person.pop("city")

print("Dictionary:", person)
