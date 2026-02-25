# empty list where all users will be stored
users = []

while True:
    print("\nEnter user information:")

    name = input("Name: ")
    age = input("Age: ")
    city = input("City: ")
    email = input("Email: ")

    # single user data as dictionary
    user_info = {
        "name": name,
        "age": age,
        "city": city,
        "email": email
    }

    # add dictionary to list
    users.append(user_info)

    more = input("Add another user? (yes/no): ").lower()
    if more != "yes":
        break

# save data to txt file
with open("users_data.txt", "w") as file:
    for index, user in enumerate(users, start=1):
        file.write(f"User {index}\n")
        file.write(f"Name  : {user['name']}\n")
        file.write(f"Age   : {user['age']}\n")
        file.write(f"City  : {user['city']}\n")
        file.write(f"Email : {user['email']}\n")
        file.write("-" * 20 + "\n")

print("\nData successfully saved to users_data.txt")
