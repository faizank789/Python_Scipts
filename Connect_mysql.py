import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a SQL query
mycursor.execute("SELECT * FROM yourtable")

# Fetch the results
results = mycursor.fetchall()

# Print the results
for row in results:
  print(row)



# mssql

import pyodbc

server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

cursor = conn.cursor()
