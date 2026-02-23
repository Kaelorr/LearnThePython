#!/usr/bin/env python3

# Dictionary practice: key-value pairs, unordered (insertion-ordered in modern Python)

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
    