#!/usr/bin/env python3
'''
dict-এ আমরা কী করতে পারি এবং কী wq করতে পারে না।
১. dict পরিবর্তনযোগ্য, আমরা আইটেম যোগ করতে, আপডেট করতে, অপসারণ করতে পারি।
২. dict কীগুলি অবশ্যই অপরিবর্তনীয় হতে হবে (str, int, tuple), মানগুলি যেকোনো ধরণের হতে পারে।
৩. dict অ-ক্রমযুক্ত (আধুনিক পাইথনে সন্নিবেশ-ক্রমযুক্ত), তাই কোনও সূচীকরণ নেই।
৪. dict দ্রুত কী-ভিত্তিক লুকআপের জন্য অপ্টিমাইজ করা হয়েছে।
৫. dict ম্যানিপুলেশন এবং অ্যাক্সেসের জন্য বিভিন্ন পদ্ধতি সমর্থন করে।
৬. dict নেস্ট করা যেতে পারে (dicts-এর মধ্যে dicts)।
৭. dict ডুপ্লিকেট কীগুলিকে অনুমতি দেয় না; শেষ অ্যাসাইনমেন্টটি জিতে যায়।
৮. dict কীগুলি হ্যাশেবল (অপরিবর্তনীয়) হতে হবে, মানগুলি পরিবর্তনযোগ্য হতে পারে।
৯. dict কীগুলির ক্রম বজায় রাখে না (আধুনিক পাইথনে সন্নিবেশ-ক্রমযুক্ত)।
১০. লক ছাড়া সমসাময়িক পরিবর্তনের জন্য dict থ্রেড-নিরাপদ নয়।
১১. dict তালিকার মতো স্লাইসিং বা ইনডেক্সিং সমর্থন করে না।
১২. dict কীগুলি অবশ্যই অনন্য হতে হবে; ডুপ্লিকেট কীগুলি পূর্ববর্তী মানগুলিকে ওভাররাইট করবে।
১৩. dict যোগ বা গুণনের মতো গাণিতিক ক্রিয়াকলাপগুলিকে সমর্থন করে না।
১৪. dict কীগুলির ক্রম বজায় রাখে না (আধুনিক পাইথনে সন্নিবেশ-ক্রমযুক্ত)।
১৫. dict হ্যাশেবল নয় এবং অন্য ডিক্টে কী হিসাবে ব্যবহার করা যাবে না।
১৬. dict কীগুলির ক্রম বজায় রাখে না (আধুনিক পাইথনে সন্নিবেশ-ক্রমযুক্ত)।'''

if __name__ == "__main__":
    print("\n--- Dict practice ---")

    # Create dict
    student = {"name": "Rafi", "age": 22, "city": "Dhaka"}
    print("Student:", student)

    # Access
    print("Name:", student["name"])
    print("Phone (safe):", student.get("phone", "N/A"))

    # Add / update
    student["phone"] = "01700000000"
    student["age"] = 23
    print("Updated:", student)

    # Remove
    student.pop("city", None)
    print("After pop:", student)

    # Iterate
    for key, value in student.items():
        print(key, "->", value)
    # del student["age"]  # also works
    del student["phone"]  # also works
    print("After del:", student)    # also works

    # Dictionary comprehension
    squares = {n: n * n for n in range(1, 6)}
    print("Squares:", squares)

    # Real-life: frequency count
    letters = ["a", "b", "a", "c", "b", "a"]
    freq = {}
    for ch in letters:
        freq[ch] = freq.get(ch, 0) + 1
    print("Frequency:", freq)

    # Real-life: phonebook lookup
    phonebook = {"Rafi": "0171", "Mita": "0181", "Nila": "0191"}
    name = "Mita"
    print("Phone:", phonebook.get(name, "Not found"))

    # Real-life: nested dict (profiles)
    users = {
        "u1": {"name": "Rafi", "roles": ["admin", "editor"]},
        "u2": {"name": "Mita", "roles": ["viewer"]},
    }
    print("User u1 roles:", users["u1"]["roles"])

    # Real-life: group items by category
    products = [
        {"name": "Laptop", "category": "Electronics"},
        {"name": "Mouse", "category": "Electronics"},
        {"name": "T-Shirt", "category": "Fashion"},
    ]
    grouped = {}
    for p in products:
        grouped.setdefault(p["category"], []).append(p["name"])
    print("Grouped products:", grouped)

    # Real-life: merge config (new values override old)
    default_cfg = {"theme": "light", "lang": "en", "timeout": 30}
    user_cfg = {"theme": "dark", "timeout": 10}
    final_cfg = {**default_cfg, **user_cfg}
    print("Final config:", final_cfg)

    # Real-life: validate required fields
    payload = {"name": "Rafi", "age": 22}
    required = {"name", "age", "phone"}
    missing = required - payload.keys()
    print("Missing fields:", missing)

    # Real-life: totals from list of dicts
    orders = [
        {"item": "pen", "qty": 2, "price": 10},
        {"item": "book", "qty": 1, "price": 120},
        {"item": "pen", "qty": 1, "price": 10},
    ]
    totals = {}
    for o in orders:
        totals[o["item"]] = totals.get(o["item"], 0) + o["qty"] * o["price"]
    print("Item totals:", totals)




dict2 = {"name": "Mita", "age": 22, "city": "Dhaka"}

for key in dict2:
    print(key, "->", dict2[key])

for key, value in dict2.items():
    print(key, "->", value) 
    

'''All function and built in methods for dict is here :
1. dict.get(key, default=None): Returns the value for the specified key if it exists, otherwise returns the default value (or None if not provided).
2. dict.keys(): Returns a view object that displays a list of all the keys in the dictionary.
3. dict.values(): Returns a view object that displays a list of all the values in the dictionary.
4. dict.items(): Returns a view object that displays a list of key-value pairs in the dictionary.
5. dict.update(other_dict): Updates the dictionary with key-value pairs from another dictionary, overwriting existing keys if they are present.
6. dict.pop(key, default=None): Removes the specified key and returns its value. If the key is not found, it returns the default value (or raises a KeyError if not provided).
7. dict.popitem(): Removes and returns an arbitrary (key, value) pair from the dictionary.
8. dict.clear(): Removes all key-value pairs from the dictionary.
9. dict.copy(): Creates a shallow copy of the dictionary.
10. dict.fromkeys(iterable, value=None): Creates a new dictionary with keys from the iterable and values set to the specified value (or None if not provided).
11. dict.setdefault(key, default=None): Returns the value for the specified key if it exists, otherwise sets the key to the default value and returns it.
12. dict.items(): Returns a view object that displays a list of key-value pairs in the dictionary.
13. dict.keys(): Returns a view object that displays a list of all the keys in the dictionary.
14. dict.values(): Returns a view object that displays a list of all the values in the dictionary.
15. dict.update(other_dict): Updates the dictionary with key-value pairs from another dictionary, overwriting existing keys if they are present.
16. dict.pop(key, default=None): Removes the specified key and returns its value. If the key is not found, it returns the default value (or raises a KeyError if not provided).
17. dict.popitem(): Removes and returns an arbitrary (key, value) pair from the dictionary.
18. dict.clear(): Removes all key-value pairs from the dictionary.
19. dict.copy(): Creates a shallow copy of the dictionary.
20. dict.fromkeys(iterable, value=None): Creates a new dictionary with keys from the iterable and values set to the specified value (or None if not provided).
21. dict.setdefault(key, default=None): Returns the value for the specified key if it exists, otherwise sets the key to the default value and returns it.
22. len(dict): Returns the number of key-value pairs in the dictionary.
23. del dict[key]: Deletes the specified key and its associated value from the dictionary.
24. in operator: Checks if a key exists in the dictionary (e.g., key in dict).
25. not in operator: Checks if a key does not exist in the dictionary (e.g., key not in dict).
26. dict comprehension: A concise way to create dictionaries using a single line of code with an optional condition.
27. dict membership: Checking if a key exists in the dictionary using the in keyword.'''
