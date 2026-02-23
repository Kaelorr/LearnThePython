#!/usr/bin/env python3

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
