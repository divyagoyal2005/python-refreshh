def contains_duplicate(numbers):
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    seen = set()

    for number in numbers:
        if number in seen:
            return True

        seen.add(number)

    return False


print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))