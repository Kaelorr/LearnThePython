#!/usr/bin/env python3

# Set practice: unordered, unique items

if __name__ == "__main__":
    print("\n--- Set practice ---")

    # Create set
    nums = {1, 2, 3, 3, 2}
    print("Set (unique):", nums)

    # Add / update
    nums.add(4)
    nums.update([5, 6])
    print("After add/update:", nums)

    # Remove / discard
    nums.discard(10)  # no error if missing
    nums.remove(3)
    print("After remove:", nums)

    # Membership
    print("Has 2:", 2 in nums)

    # Set operations
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print("Union:", a | b)
    print("Intersection:", a & b)
    print("Difference:", a - b)
    print("Symmetric diff:", a ^ b)

    # Real-life: remove duplicates from list
    items = ["pen", "pencil", "pen", "eraser"]
    unique_items = list(set(items))
    print("Unique items:", unique_items)

    # Real-life: common courses
    student1 = {"Math", "Science", "English"}
    student2 = {"Math", "History", "English"}
    common = student1 & student2
    print("Common courses:", common)

    # Set comprehension
    squares = {n * n for n in range(1, 6)}
    print("Squares:", squares)

    # Real-life: permissions check (subset)
    required = {"read", "write"}
    user_perms = {"read", "write", "delete"}
    print("Has required perms:", required <= user_perms)

    # Real-life: blocked words filter
    blocked = {"bad", "spam"}
    words = ["this", "is", "spam", "free"]
    clean_words = [w for w in words if w not in blocked]
    print("Clean words:", clean_words)

    # Real-life: unique visitors count
    visits = ["u1", "u2", "u1", "u3", "u2"]
    unique_visitors = set(visits)
    print("Unique visitors:", len(unique_visitors))

    # Real-life: set of tuples (unique coordinates)
    coords = {(0, 0), (1, 2), (0, 0), (2, 3)}
    print("Unique coords:", coords)

    # Real-life: frozenset as dict key (groups)
    group_scores = {
        frozenset({"A", "B"}): 80,
        frozenset({"A", "C"}): 90,
    }
    print("Group score (A,B):", group_scores[frozenset({"A", "B"})])
