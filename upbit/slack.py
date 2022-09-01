import requests

# Send a message whatever I want to my slack channel
def alarm(text):
    slack = {"token" : "xoxb-3895104489537-4012924262898-iqInhdludJeMINTjKcqJfhoc",
    "channel" : "#trading-alarm"}
    
    requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+ slack['token']},
        data={"channel": slack['channel'],"text": text})