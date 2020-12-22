from slack_sdk.rtm import RTMClient


# Variables used for code
token = ""
phrase = "realm-status"

# This is the actual listener
client = RTMClient(token=token)


# Function to read messages and do stuff
@RTMClient.run_on(event="message")
def got_message(**payload):
    # Let's ignore bot-messages (these are events from bots, aka ourself responding to slack)
    print(f"Message Received: {payload['data']}")
    data = payload['data']
    web_client = payload['web_client']
    channel_id = data['channel']
    thread_ts = data['ts']
    if phrase in data['text']:
        print(f"Message contains {phrase}\tMessage: {data['text']}")

        # Call function that gets status and returns string here
        # response = get_realm_status()

        # Now we respond back to slack with status (Update to use response above => 'text = f"Realm Status Is: {response}")
        web_client.chat_postMessage(channel=channel_id, text=f"Realm Status Is: ()")

        # If you want response to be in a thread of the parent message, use this one
        # web_client.chat_postMessage(channel=channel_id, text=f"Realm Status Is: ()", thread_ts=thread_ts)
# Start the RTM Client to get messages

client.start()
print("Connected To Slack")
