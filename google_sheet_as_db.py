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
