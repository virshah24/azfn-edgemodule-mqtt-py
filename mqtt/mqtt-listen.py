import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################

broker_address="broker.mqttdashboard.com" 
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("mskoch-mqtt-test") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")

client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
time.sleep(60) # wait
client.loop_stop() #stop the loop