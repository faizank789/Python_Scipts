import os
import time
import slack

slack_token = os.environ["SLACK_API_TOKEN"]
client = slack.WebClient(token=slack_token)

# Keep the bot running and connected to Slack
while True:
    try:
        # Your code to listen for and respond to events goes here
        # ...

        time.sleep(1)
    except Exception as e:
        print("Error:", e)
        time.sleep(5)
