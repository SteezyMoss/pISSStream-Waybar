from lightstreamer.client import *
import time
import json

sub = Subscription("MERGE",["NODE3000005"],["Value"])
sub.setRequestedSnapshot("yes")

gValue = -1 
gStatus = "Disconnected"

class SubListener(SubscriptionListener):
    def onItemUpdate(self, update): 
        global gValue
        gValue = update.getValue("Value") 

    def onListenStart(self):
        #print("Listen Started")
        pass

    def onSubscription(self):
        #print("Subscribed!")
        global gStatus
        gStatus = "Connected"

    def onSubscriptionError(self, code, message):
        #print(code, message)
        pass


class ClientSpy(ClientListener):
    def onServerError(self, code, message):
        #print(f"Spy Error: {code}, {message}")
        pass


sub.addListener(SubListener())

client = LightstreamerClient("https://push.lightstreamer.com", "ISSLIVE")
client.addListener(ClientSpy())
client.connect()
client.subscribe(sub)

time.sleep(3)


if gValue == -1:
    p = "N/A"
else:
    p = f"{str(gValue)}%"


try:
    print(json.dumps({"text": p, "tooltip": gStatus}), flush=True)
except Exception:
    print(json.dumps({"text": "N/A", "tooltip": "N/A"}))
    
