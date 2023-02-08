from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

def upload_video_to_youtube(video_file_path, video_title, video_description):
    try:
        # Get the user's Google credentials
        credentials = Credentials.from_authorized_user_file("client_secrets.json")

        # Build the YouTube service
        youtube = build('youtube', 'v3', credentials=credentials)

        # Create a MediaFileUpload object for the video file
        video = MediaFileUpload(video_file_path, chunksize=-1, resumable=True)

        # Define the video metadata (title, description, etc.)
        body = {
            'snippet': {
                'title': video_title,
                'description': video_description
            },
            'status': {
                'privacyStatus': 'private'
            }
        }

        # Insert the video into the YouTube service
        video_insert_response = youtube.videos().insert(
            part=','.join(body.keys()),
            body=body,
            media_body=video
        ).execute()

        print(f'Video with ID {video_insert_response["id"]} was successfully uploaded to YouTube.')

    except HttpError as error:
        print(f'An error occurred while uploading the video to YouTube: {error}')

if __name__ == '__main__':
    video_file_path = 'path/to/your/video.mp4'
    video_title = 'Your Video Title'
    video_description = 'Your Video Description'
    upload_video_to_youtube(video_file_path, video_title, video_description)
