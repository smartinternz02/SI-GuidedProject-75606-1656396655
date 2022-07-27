#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "e4iq2b",
        "typeId": "UNO_R3",
        "deviceId":"20L201"
    },
    "auth": {
        "token": "8Q7W?U!Cori+UKG*uw"
    }
}
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if m=="fanon":
        print("The Fan is turned ON")
    elif m=="fanoff":
        print("The Fan is Terned OFF")
    elif m=="pumpon":
        print("The Pump is Terned ON")
    elif m=="pumpoff":
        print("ThePump is Terned OFF")
    elif m=="intensityinc":
        print("The Intensity is Increased")
    elif m=="intensitydec":
        print("The Intensity is Decreased")
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
 
while True:
    temp=random.randint(0,40)
    hum=random.randint(20,90)
    amo=random.randint(0,50)
    water= random.randint(0,100)
    fire=random.randint( 0,100)
    intensity=random.randint(0,100)
    myData={'d':{'temperature':temp, 'humidity':hum, 'Amonia':amo,'Water':water,'Fire':fire,'Intensity':intensity}}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(10)
client.disconnect()
