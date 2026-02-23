#!/usr/bin/env python3

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
