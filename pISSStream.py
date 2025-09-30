from lightstreamer.client import *
import time
import json

# Subscribing to the urine tanks field/item and requesting the initial snapshot
sub = Subscription("MERGE",["NODE3000005"],["Value"])
sub.setRequestedSnapshot("yes")

# Setting lazy global variables for tracking tank value and subscription status
gValue = -1 
gStatus = "Disconnected"


# Defining the subscription listener and configuring necessary signals
class SubListener(SubscriptionListener):
    def onItemUpdate(self, update): 
        global gValue
        gValue = update.getValue("Value") 

    def onSubscription(self):
        global gStatus
        gStatus = "Connected"


sub.addListener(SubListener())

client = LightstreamerClient("https://push.lightstreamer.com", "ISSLIVE")
client.connect()
client.subscribe(sub)

# Added this to ensure the client has time to connect, subscribe, and snapshot before printing
time.sleep(2)


# Checking if gValue received an update from... space, that is an interesting thought
if gValue == -1:
    p = "N/A"
else:
    try:
        p = f"{str(gValue)}%"
    except Exception:
        p = "N/A"


# Output p and gStatus as a json for waybar
print(json.dumps({"text": p, "tooltip": gStatus}), flush=True)


