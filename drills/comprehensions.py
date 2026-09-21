# 1. List comprehension: filter evens

numbers = range(1, 21)
evens = [n for n in numbers if n % 2 == 0]


# 2. List comprehension: transform strings

words = ["python", "git", "vscode"]
uppercase_words = [word.upper() for word in words]


# 3. List comprehension: nested flatten

nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for group in nested for item in group]


# 4. Dictionary comprehension: character frequency

text = "banana"
char_frequency = {
    char: text.count(char)
    for char in set(text)
}


# 5. Dictionary comprehension: swap key-values

original = {"a": 1, "b": 2, "c": 3}
swapped = {
    value: key
    for key, value in original.items()
}


# 6. Set comprehension: unique domains

emails = [
    "alice@gmail.com",
    "bob@yahoo.com",
    "carol@gmail.com",
]

domains = {
    email.split("@")[1]
    for email in emails
}


print("Evens:", evens)
print("Uppercase:", uppercase_words)
print("Flattened:", flattened)
print("Character frequency:", char_frequency)
print("Swapped:", swapped)
print("Domains:", domains)
