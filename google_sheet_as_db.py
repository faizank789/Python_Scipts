import gspread
from oauth2client.service_account import ServiceAccountCredentials

# authenticate using the service account key
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
gc = gspread.authorize(credentials)

# open the Google Sheet
sheet = gc.open("User Database").sheet1

# add a new user to the sheet
sheet.append_row(["Faizan", "123 london St", "55478-44-44", "12345"])


# Create a new Google Sheet and name it appropriately.
# Define the columns for storing user information such as "Name", "Address", "Phone Number", and "ID".
# Write a Python script that interacts with the Google Sheets API to add, retrieve, update, and delete user information.
# To get started with the Google Sheets API, you'll need to create a project in the Google Cloud Console, enable the Google Sheets API, and generate credentials in the form of a service account key.
# Once you have the credentials, you can use the google-auth and gspread libraries in Python to interact with the Google Sheets API.
