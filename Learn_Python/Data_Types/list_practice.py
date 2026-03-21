#!/usr/bin/env python3
''' what we can do with list data type in python 
List is an ordered collection of items. It is mutable, meaning you can change its contents after creation.
'''
# List practice: ordered, mutable, allows duplicates

if __name__ == "__main__":
    print("\n--- List practice ---")

    # Create list
    numbers = [1, 2, 3, 4, 5]
    print("Numbers:", numbers)

    # Access + slicing
    print("First:", numbers[0])
    print("Last 3:", numbers[-3:])

    # Append / insert / extend
    numbers.append(6)
    numbers.insert(0, 0)
    numbers.extend([7, 8])
    print("After add:", numbers)

    # Remove / pop
    numbers.remove(3)
    last = numbers.pop()
    print("After remove/pop:", numbers, "popped:", last)

    # Sort / reverse
    numbers.sort()
    numbers.reverse()
    print("Sorted desc:", numbers)

    # List comprehension (filter)
    evens = [n for n in numbers if n % 2 == 0]
    print("Evens:", evens)

    # Transform (map-like)
    squares = [n * n for n in numbers]
    print("Squares:", squares)

    # Enumerate
    fruits = ["apple", "banana", "mango"]
    for i, fruit in enumerate(fruits, start=1):
        print(f"{i}. {fruit}")

    # Join / split
    joined = ", ".join(fruits)
    print("Joined:", joined)
    back = joined.split(", ")
    print("Split:", back)

    # Real-life: clean input
    raw_names = ["  Rafi ", "", "Mita", "  ", "Nila"]
    names = [n.strip() for n in raw_names if n.strip()]
    print("Clean names:", names)

    # Real-life: unique while keeping order
    items = ["pen", "pencil", "pen", "eraser", "pencil"]
    seen = set()
    unique_items = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    print("Unique items:", unique_items)

    # Real-life: chunking (pagination)
    nums = list(range(1, 11))
    size = 4
    chunks = [nums[i:i + size] for i in range(0, len(nums), size)]
    print("Chunks:", chunks)

    # Real-life: find index by condition
    idx = next((i for i, v in enumerate(nums) if v > 7), -1)
    print("First index > 7:", idx)

    # Real-life: partition list (pass/fail)
    marks = [33, 75, 40, 28, 90]
    passed = [m for m in marks if m >= 40]
    failed = [m for m in marks if m < 40]
    print("Passed:", passed, "Failed:", failed)

    # Real-life: stable sort by key (list of dicts)
    students = [
        {"name": "Rafi", "score": 88},
        {"name": "Mita", "score": 92},
        {"name": "Nila", "score": 75},
    ]
    students_sorted = sorted(students, key=lambda x: x["score"], reverse=True)
    print("Sorted students:", students_sorted)

    # Real-life: flatten nested list (one level)
    matrix = [[1, 2], [3, 4], [5]]
    flat = [x for row in matrix for x in row]
    print("Flatten:", flat)

    # Real-life: sliding window average (3-day)
    temps = [30, 32, 31, 29, 33, 34]
    window = 3
    moving_avg = [
        sum(temps[i:i + window]) / window
        for i in range(len(temps) - window + 1)
    ]
    print("Moving average:", moving_avg)

    # Real-life: combine two lists (name + score)
    names = ["A", "B", "C"]
    scores = [80, 70, 90]
    report = [f"{n}: {s}" for n, s in zip(names, scores)]
    print("Report:", report)


''' All function and built in methods for list is here : 
1. append(): Adds an element to the end of the list.
2. insert(): Inserts an element at a specified position in the list.
3. extend(): Extends the list by appending elements from another iterable.
4. remove(): Removes the first occurrence of a specified value from the list.
5. pop(): Removes and returns the element at a specified position (default is the last element).
6. clear(): Removes all elements from the list.
7. index(): Returns the index of the first occurrence of a specified value.
8. count(): Returns the number of occurrences of a specified value in the list.
9. sort(): Sorts the list in ascending order (by default).
10. reverse(): Reverses the order of the elements in the list.
11. copy(): Creates a shallow copy of the list.
12. len(): Returns the number of elements in the list.
13. min(): Returns the smallest element in the list.
14. max(): Returns the largest element in the list.
15. sum(): Returns the sum of all elements in the list.
16. sorted(): Returns a new sorted list without modifying the original.
17. reversed(): Returns an iterator that accesses the elements of the list in reverse order.
18. enumerate(): Returns an iterator that produces pairs of index and value from the list.
19. zip(): Combines elements from multiple iterables into tuples.
20. list(): Creates a new list from an iterable.
21. any(): Returns True if any element of the list is true.
22. all(): Returns True if all elements of the list are true.
23. map(): Applies a function to every item of the list and returns a list of the results.
24. filter(): Constructs a list from those elements of the list for which a function returns true.
25. reduce(): Applies a rolling computation to sequential pairs of values in the list (from functools import reduce).
26. list comprehension: A concise way to create lists using a single line of code with an optional condition.
27. slicing: A powerful way to access a range of elements in the list using the syntax list[start:stop:step].
28. list concatenation: Combining two or more lists using the + operator.
29. list replication: Creating a new list by repeating an existing list a specified number of times using the * operator.
30. list membership: Checking if an element exists in the list using the in keyword.'''