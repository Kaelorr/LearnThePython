#!/usr/bin/env python3
''' what we can do with set data type in python 
Set is an unordered collection of unique items. It is mutable, meaning you can add or remove items after creation.
 Sets are useful for membership testing, eliminating duplicates, and performing mathematical set operations like union, intersection, and difference.'''

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



'''All function and built in methods for set is here :
1. add(): Adds an element to the set.
2. update(): Adds multiple elements to the set from an iterable (like a list).
3. remove(): Removes a specific element from the set. Raises a KeyError if the element is not found.
4. discard(): Removes a specific element from the set if it exists. Does not raise an error if the element is not found.
5. clear(): Removes all elements from the set.
6. union(): Returns a new set that is the union of two sets (all unique elements from both sets).
7. intersection(): Returns a new set that is the intersection of two sets (elements present in both sets).
8. difference(): Returns a new set that is the difference between two sets (elements in the first set but not in the second).
9. symmetric_difference(): Returns a new set that is the symmetric difference of two sets (elements in either set, but not both).
10. issubset(): Returns True if all elements of the set are present in another set.
11. issuperset(): Returns True if the set contains all elements of another set.
12. isdisjoint(): Returns True if two sets have no common elements.
13. copy(): Returns a shallow copy of the set.
14. pop(): Removes and returns an arbitrary element from the set.
15. len(): Returns the number of elements in the set.
16. set(): Creates a new set from an iterable.
17. frozenset(): Creates an immutable version of a set.
18. set comprehension: A concise way to create sets using a single line of code with an optional condition.
19. in operator: Checks if an element exists in the set.
20. not in operator: Checks if an element does not exist in the set.
21. set membership: Checking if an element exists in the set using the in keyword.'''