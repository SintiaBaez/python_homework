import pandas as pd 
import numpy as np
import json

# TASK 1: Introduction to Pandas - Creating and Manipulating DataFrames
# Create a DataFrame from a dictionary:

data = {
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 35],
'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert the dictionary into a DataFrame using Pandas
task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)


# Add a new column:
task1__with_salary = task1_data_frame.copy()
task1__with_salary['Salary'] = [70000, 80000, 90000]
print(task1__with_salary)

# Modify an existing column:
task1_older = task1__with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print(task1_older)

# Save the DataFrame as a CSV file:
task1_older.to_csv("employees.csv", index=False)
task1_older = pd.read_csv('employees.csv')
print(task1_older.head)

# TASK 2: Loading Data from CSV and JSON

# Read data from a CSV file:
task2_employees = pd.read_csv('employees.csv')
print(task2_employees.head())

# Read data from a JSON file:

json_employees = pd.read_json('additional_employees.json')
print(json_employees.head())

# Combine DataFrames:

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees.head())

# TASK 3: Data Inspection - Using Head, Tail, and Info Methods

# Use the head() method:
fist_three = more_employees.head(3)
print(fist_three)

# Use the tail() method:

last_two = more_employees.tail(2)
print(last_two)

# Get the shape of a DataFrame

employees_shape = more_employees.shape
print(employees_shape)

# Use the info() method:

more_employees_info = more_employees.info()
print(more_employees_info)


# TASK 4: Data Cleaning

# Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.

dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data.head())
clean_data = dirty_data.copy()

# Remove any duplicate rows from the DataFrame
clean_data = clean_data.drop_duplicates()
print("Duplicates removed:")
print(clean_data.head())

# Convert Age to numeric and handle missing values

clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
print("Missing values handled:")
print(clean_data.head())

# Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN

clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].mean())
print("Salary converted to numeric:")
print(clean_data.head())

#   Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print("Missing numeric values filled:")
print(clean_data.head())

# Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("Hire Date converted to datetime:")
print(clean_data.head())

# Strip extra whitespace and standardize Name and Department as uppercase

clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("Whitespace stripped and standardized:")
print(clean_data.head())







