import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################

broker_address="localhost" 
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("local-mqtt-py") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")

client.connect(broker_address) #connect to broker
client.loop_start() #start the loop

print("Subscribing to topic","localedge/local-py")
client.subscribe("localedge/local-py", qos=0)
print("Publishing message to topic","localedge/local-py")
client.publish("localedge/local-py","alert")#publish
time.sleep(4) # wait
client.loop_stop() #stop the loop