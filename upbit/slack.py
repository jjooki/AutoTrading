import requests
import os

# Send a message whatever I want to my slack channel
def alarm(text):
    token = os.environ['SLACK_TOKEN']
    slack = {"token" : token,
    "channel" : "#trading-alarm"}
    
    requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+ slack['token']},
        data={"channel": slack['channel'],"text": text})