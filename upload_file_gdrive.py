from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Use the credentials to build the Drive API client
creds = Credentials.from_service_account_file("path/to/credentials.json")
service = build("drive", "v3", credentials=creds)

# Create the file metadata
file_metadata = {
    'name': 'example.txt'
}

# Read the contents of the file
media = MediaFileUpload('example.txt',
                        mimetype='text/plain')

# Upload the file
file = service.files().create(body=file_metadata, media_body=media,
                              fields='id').execute()
print(F'File ID: {file.get("id")}')



# You can upload a file to Google Drive using the Google Drive API. 
# To do this, you need to first set up a Google Drive API project 
# and obtain the necessary credentials (e.g., a client ID and secret). Then, 
# you can use the API to upload the file to your Google Drive account.
