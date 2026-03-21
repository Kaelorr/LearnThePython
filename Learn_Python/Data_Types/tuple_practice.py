#!/usr/bin/env python3
''' examples of using tuple data type in python
Tuple is an ordered collection of items. It is immutable, meaning you cannot change its contents after creation. 
Tuples are useful for grouping related data together and can be used as keys in dictionaries due to their immutability. 
They support indexing, slicing, and various built-in methods for accessing and'''
# Tuple practice: ordered, immutable, hashable

if __name__ == "__main__":
    print("\n--- Tuple practice ---")

    # Create tuple
    point = (10, 20)
    print("Point:", point)

    # Single item tuple
    single = (5,)
    print("Single tuple:", single)

    # Unpacking
    x, y = point
    print("Unpacked:", x, y)

    # Swap using tuple unpacking
    a, b = 5, 9
    a, b = b, a
    print("Swapped:", a, b)

    # Return multiple values
    def stats(nums):
        return min(nums), max(nums), sum(nums) / len(nums)

    values = [10, 20, 5, 35]
    min_v, max_v, avg_v = stats(values)
    print("Stats:", min_v, max_v, avg_v)

    # Tuple as dict key (hashable)
    temps = {("Dhaka", "Mon"): 30, ("Dhaka", "Tue"): 29}
    print("Temp Dhaka Mon:", temps[("Dhaka", "Mon")])

    # List of tuples (records)
    students = [("A", 80), ("B", 70), ("C", 90)]
    students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
    print("Sorted by score:", students_sorted)

    # Constants
    WEEKDAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    print("Weekdays:", WEEKDAYS)

    # Real-life: date as tuple
    date = (2026, 2, 23)
    print("Date:", date)

    # Real-life: grid positions
    grid = {(0, 0): "S", (0, 1): ".", (1, 1): "E"}
    print("Grid start:", grid[(0, 0)])

    # Real-life: tuple packing/unpacking with *rest
    data = (1, 2, 3, 4, 5)
    first, *middle, last = data
    print("First:", first, "Middle:", middle, "Last:", last)

    # Real-life: caching with tuple key
    cache = {}
    x, y = 3, 4
    cache[(x, y)] = x * y
    print("Cache for (3,4):", cache[(3, 4)])

    # Real-life: comparing time tuples (HH, MM)
    start = (9, 30)
    end = (17, 0)
    print("Start before end:", start < end)

    # Real-life: zip to build tuples
    names = ["A", "B", "C"]
    scores = [80, 70, 90]
    rows = list(zip(names, scores))
    print("Rows:", rows)

    # Real-life: immutable config
    DB_CONFIG = ("localhost", 5432, "app_db")
    print("DB config:", DB_CONFIG)


''' All function and built in methods for tuple is here :
1. len(tuple): Returns the number of items in the tuple.
2. tuple[index]: Accesses the item at the specified index (0-based).
3. tuple[start:stop:step]: Slices the tuple to return a new tuple containing the specified range of items.
4. tuple.count(value): Returns the number of occurrences of the specified value in the tuple.
5. tuple.index(value): Returns the index of the first occurrence of the specified value in the tuple. Raises a ValueError if the value is not found.
6. tuple + tuple: Concatenates two tuples to create a new tuple.
7. tuple * n: Repeats the tuple n times to create a new tuple.
8. in operator: Checks if a value exists in the tuple (e.g., value in tuple).
9. not in operator: Checks if a value does not exist in the tuple (e.g., value not in tuple).
10. tuple(): Creates a new tuple from an iterable (like a list).
11. unpacking:  Allows you to assign the items of a tuple to individual variables (e.g., a, b = tuple).
12. zip(): Combines multiple iterables into a tuple of tuples, where each tuple contains the corresponding elements from the input iterables.
13. sorted(): Returns a new sorted list of the items in the tuple without modifying the original tuple.
14. min(tuple): Returns the smallest item in the tuple.
15. max(tuple): Returns the largest item in the tuple.
16. sum(tuple): Returns the sum of all items in the tuple (only for numeric tuples).
17. any(tuple): Returns True if any item in the tuple is true (non-zero, non-empty, etc.).
18. all(tuple): Returns True if all items in the tuple are true.
19. tuple comprehension: A concise way to create tuples using a single line of code with an optional condition (e.g., tuple(x**2 for x in range(5))).
20. slicing: A powerful way to access a range of items in the tuple using the syntax tuple[start:stop:step].
21. tuple concatenation: Combining two or more tuples using the + operator.
22. tuple replication: Creating a new tuple by repeating an existing tuple a specified number of times using the * operator.
23. tuple membership: Checking if a value exists in the tuple using the in keyword.
24. tuple unpacking with *rest: Allows you to unpack a tuple into variables while collecting the remaining items into a list (e.g., first, *rest = tuple).
25. tuple as dict key: Since tuples are immutable and hashable, they can be used as keys in dictionaries to represent composite keys (e.g., grid positions, date tuples, etc.).
26. tuple immutability: Once a tuple is created, its contents cannot be changed. This makes tuples useful for representing fixed collections of items, such as coordinates, configurations, or records that'''