#!/usr/bin/env python
# coding: utf-8

# In[6]:


import mysql.connector
from mysql.connector import Error

# Replace these with your connection details
connection_config_dict = {
    'user': 'root',
    'password': 'Root@123',
    'host': 'localhost',
    'database': 'payroll_management_system'
}

try:
    # Connect to the database
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        print('Connected to MySQL database')
        cursor = connection.cursor()

        # Query the database
        query = "SELECT * FROM Employees LIMIT 10;"  # Replace with your query
        cursor.execute(query)
        
        # Fetch the data
        records = cursor.fetchall()
        print(f"Displaying rows from {cursor.column_names}:")

        # Present data to the screen
        for row in records:
            print(row)
        
        # Write data to a text file
        with open('employees_report.txt', 'w') as f:
            for row in records:
                f.write(str(row) + "\n")
        
        print("Data written to 'employees_report.txt'")
        print("")

except Error as e:
    print(f"Error: {e}")

try:
    # Connect to the database
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        print('Connected to MySQL database')
        cursor = connection.cursor()

        # Query the database
        query = "SELECT * FROM Departments LIMIT 10;"  # Replace with your query
        cursor.execute(query)
        
        # Fetch the data
        records = cursor.fetchall()
        print(f"Displaying rows from {cursor.column_names}:")

        # Present data to the screen
        for row in records:
            print(row)
        
        # Write data to a text file
        with open('departments.txt', 'w') as f:
            for row in records:
                f.write(str(row) + "\n")
        
        print("Data written to 'departments.txt'")
        print("")

except Error as e:
    print(f"Error: {e}")
    
try:
    # Connect to the database
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        print('Connected to MySQL database')
        cursor = connection.cursor()

        # Query the database
        query = "SELECT * FROM bankinformation LIMIT 10;"  # Replace with your query
        cursor.execute(query)
        
        # Fetch the data
        records = cursor.fetchall()
        print(f"Displaying rows from {cursor.column_names}:")

        # Present data to the screen
        for row in records:
            print(row)
        
        # Write data to a text file
        with open('bankinformation.txt', 'w') as f:
            for row in records:
                f.write(str(row) + "\n")
        
        print("Data written to 'bankinformation.txt'")
        print("")

except Error as e:
    print(f"Error: {e}")
    
try:
    # Connect to the database
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        print('Connected to MySQL database')
        cursor = connection.cursor()

        # Query the database
        query = "SELECT * FROM attendance LIMIT 10;"  # Replace with your query
        cursor.execute(query)
        
        # Fetch the data
        records = cursor.fetchall()
        print(f"Displaying rows from {cursor.column_names}:")

        # Present data to the screen
        for row in records:
            print(row)
        
        # Write data to a text file
        with open('attendance.txt', 'w') as f:
            for row in records:
                f.write(str(row) + "\n")
        
        print("Data written to 'attendance.txt'")
        print("")

except Error as e:
    print(f"Error: {e}")
    
try:
    # Connect to the database
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        print('Connected to MySQL database')
        cursor = connection.cursor()

        # Query the database
        query = "SELECT * FROM deductions LIMIT 10;"  # Replace with your query
        cursor.execute(query)
        
        # Fetch the data
        records = cursor.fetchall()
        print(f"Displaying rows from {cursor.column_names}:")

        # Present data to the screen
        for row in records:
            print(row)
        
        # Write data to a text file
        with open('deductions.txt', 'w') as f:
            for row in records:
                f.write(str(row) + "\n")
        
        print("Data written to 'deductions.txt'")
        print("")

except Error as e:
    print(f"Error: {e}")
    
try:
    # Connect to the database
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        print('Connected to MySQL database')
        cursor = connection.cursor()

        # Query the database
        query = "SELECT * FROM employeeallowances LIMIT 10;"  # Replace with your query
        cursor.execute(query)
        
        # Fetch the data
        records = cursor.fetchall()
        print(f"Displaying rows from {cursor.column_names}:")

        # Present data to the screen
        for row in records:
            print(row)
        
        # Write data to a text file
        with open('employeeallowances.txt', 'w') as f:
            for row in records:
                f.write(str(row) + "\n")
        
        print("Data written to 'employeeallowances.txt'")
        print("")

except Error as e:
    print(f"Error: {e}")
    
try:
    # Connect to the database
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        print('Connected to MySQL database')
        cursor = connection.cursor()

        # Query the database
        query = "SELECT * FROM employeedeductions LIMIT 10;"  # Replace with your query
        cursor.execute(query)
        
        # Fetch the data
        records = cursor.fetchall()
        print(f"Displaying rows from {cursor.column_names}:")

        # Present data to the screen
        for row in records:
            print(row)
        
        # Write data to a text file
        with open('employeedeductions.txt', 'w') as f:
            for row in records:
                f.write(str(row) + "\n")
        
        print("Data written to 'employeedeductions.txt'")
        print("")

except Error as e:
    print(f"Error: {e}")
    
try:
    # Connect to the database
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        print('Connected to MySQL database')
        cursor = connection.cursor()

        # Query the database
        query = "SELECT * FROM salarydetails LIMIT 10;"  # Replace with your query
        cursor.execute(query)
        
        # Fetch the data
        records = cursor.fetchall()
        print(f"Displaying rows from {cursor.column_names}:")

        # Present data to the screen
        for row in records:
            print(row)
        
        # Write data to a text file
        with open('salarydetails.txt', 'w') as f:
            for row in records:
                f.write(str(row) + "\n")
        
        print("Data written to 'salarydetails.txt'")
        print("")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection is closed')



# In[ ]:




