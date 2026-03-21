import csv

with open('people-1000000.csv','r') as file:
    csv_reader = csv.reader(file)
    # next(csv_reader) # skip the header row
    # next(csv_reader) # skip the header row
    # next(csv_reader) # skip the header row
    # for row in csv_reader:
    #     print(row[2:4])
# csv dictreader
with open('people-1000000.csv','r') as file:
    csv_dict_reader = csv.DictReader(file)
    for row in csv_dict_reader:
        print(row['Last Name'])
# csv DICTwriter
with open('new-1000000.csv','w') as file:
    fieldnames = ['first_name', 'last_name']
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_dict_writer.writeheader()
    with open('people-1000000.csv','r') as file:
        csv_dict_reader = csv.DictReader(file)
        for row in csv_dict_reader:
            csv_dict_writer.writerow(row)