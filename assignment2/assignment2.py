# Task 2: Read a CSV File

import csv

def read_employees():
    data = {}
    rows = []

    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)

        data["rows"] = rows
        return data

    except FileNotFoundError:
        print("Error: The file '../csv/employees.csv' was not found.")
        exit(1)
    except csv.Error:
        print("Error: The file '../csv/employees.csv' could not be read as a CSV.")
        exit(1)

# Task 3: Find the Column Index
def column_index(column_name):
    try:
        return employees["fields"].index(column_name)
    except ValueError:
        print(f"Error: The column '{column_name}' not found in employees['fields'].")
        exit(1)


employees = read_employees()
employee_id_column = column_index("employee_id")

print(f"Employee ID column index: {employee_id_column}")

# Task 4: Find the employee first name
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

print(first_name(0))

# Task 5: Find the employee: a function in a function
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == int(employee_id)

    matches = list(filter(employee_match, employees["rows"]))
    return matches

print(employee_find(3))

# Task 6: Find the emmployee with Lambda 
def employee_find_2(employee_id):
    return list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
print(employee_find_2(4))

# Task 7 : Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]
print(sort_by_last_name())

# Task 8: Create a dict for an Employee
def employee_dict(row):
    employee_data = dict(zip(employees["fields"], row))
    
    employee_data.pop("employee_id", None)
    
    return employee_data

sample_row = employees["rows"][1]
print(employee_dict(sample_row))

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    return {
        row[column_index("employee_id")]: employee_dict(row)
        for row in employees["rows"]
    }

print(all_employees_dict()) 

# Task 10: Use the os Module

import os  

def get_this_value():
    return os.getenv("THISVALUE")

print(get_this_value())

# Task 11: Creating your own module

import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Alohamora")
print(custom_module.secret)

# Task 12: Read minute1.csv and minute2.csv
import csv

def read_csv_to_dict(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        fields = next(reader)
        rows = [tuple(row) for row in reader]
    return {"fields": fields, "rows": rows}
def read_minutes():
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2
# Read the minutes CSVs
minutes1, minutes2 = read_minutes()

print("Minutes1:", minutes1)
print("Minutes2:", minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])
    combined_set = set1.union(set2)
    
    return combined_set
minutes_set = create_minutes_set()

print("Combined Minutes Set:", minutes_set)

# Task 14: Convert to datetime  

from datetime import datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    
    return minutes_list

minutes_list = create_minutes_list()

print("Minutes List:", minutes_list)

# Task 15: Write Out Sorted List

import csv
from datetime import datetime

def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])

    formatted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))

    with open("./minutes.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(formatted_list)

    return formatted_list 

converted_list = write_sorted_list()
print("Converted List:", converted_list)

with open("./minutes.csv", "r") as f:
    print(f.read())
    