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
