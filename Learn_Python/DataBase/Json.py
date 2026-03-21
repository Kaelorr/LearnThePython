import json


pp_data = '''{"people": [
     {"name": "John Doe",
     "age": 30,
     "city": "New York"
     },
     {"name": "Jane Smith",
     "age": 25,
     "city": "San Francisco"
     }
]
}'''
# text = json.loads(pp_data)
# print(text)
# with open("people.json", "w") as file:
#     json.dump(text, file, indent=4)

# with open("people.json", "w") as file:
#     del text["people"][0]
#     json.dump(text, file, indent=4)

from urllib.request import urlopen

with urlopen("https://jsonplaceholder.typicode.com/users") as response:
    data = json.load(response)
    # print(data)
# print(json.dumps(data, indent=4))
print(data[0]["name"])  # প্রথম user-এর id


with open("people-1000000.csv", "w") as file:
    json.dump(data, file, indent=4)































# text = json.dumps(pp_data, indent=6)
# print(text)


# data = json.loads(pp_data)
# print(json.loads(pp_data))
# print(type(data))
data = {"name": "Mahfuz", "age": 25, "city": "Sylhet"}
# '''indent=4 is used to make the json data more readable by adding indentation and newlines. what is the 4 in indent=4? ans: The number 4 in indent=4 specifies the number of spaces to use for each level of indentation in the resulting JSON string. This means that each nested level in the JSON structure will be indented by 4 spaces, making it easier to read and understand the hierarchy of the data. For example, if you have a JSON object with nested objects or arrays, using indent=4 will help visually distinguish between different levels of the structure, improving readability.'''
# text = json.dumps(data, indent=4)
# print(text)

# with open("data.json", "w") as file:
#     json.dump(text, file, indent=4)
