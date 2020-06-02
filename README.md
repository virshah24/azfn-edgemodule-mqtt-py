
> # Azure Function module that forks data from Azure IoT Hub on the edge to on-prem MQTT broker

>## **Abstract:**
Microsoft Azure IoT Hub provides out-of-the-box capabilities to send device-to-cloud messages directly into Azure for advanced logging/routing and generating actions based on events occurring on the edge. However, many customers, for example, in manufacturing domain adopt [PURDUE model](https://en.wikipedia.org/wiki/Purdue_Enterprise_Reference_Architecture) in their plant IoT implementations. And one of the frequent requirements is to allow Azure IoT hub to send data to their internal MQTT brokers, especially to allow communication between PURDUE's Level 2 (Control Systems) to Level 4 (Business Planning) . However, this scenario is not just limited to manufacturing domain.
>## **Challenge / Gap:**
Although [Azure IoT Hub itself supports MQTT end-points](https://techcommunity.microsoft.com/t5/internet-of-things/using-mqtt-protocol-to-communicate-with-azure-iot-hub-without/ba-p/959354) for direct communication, it doesn't provide out-of-the-box capability to post messages to "*customer managed*" local MQTT brokers. This solution addresses this gap, using PaaS services like Azure Functions on the edge.
>## **Set up:**
We need to set up / install following components and environments:
1. Set up [Azure IoT Hub](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-create-through-portal) via Azure portal.
2. Install Azure IoT-Edge runtime on the device- I am using [Linux containers on Windows](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-windows-with-linux). Also, follow the link to [Create and register IoT edge device](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-register-device) 
3. Set up VS Code with [Azure IoT Tools](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-tools) plug-in extension pack
4. Set up eclipse-mosquitto MQTT broker Docker instance on the same edge runtime device.

		 docker pull eclipse-mosquitto
6. Then the container basic Docker image with following settings. Please note **--network** switch to make sure that MQTT broker and Azure IoT Runtime network are in the same network.

		 docker run -it -p 1883:1883 -p 9001:9001 --network=azure-iot-edge eclipse-mosquitto

Note: Azure IoT edge runtime creates new network called "*azure-iot-edge*" when setting up docker images. You can check this using following Docker command.
			 
		docker network ls

7. Download [MQTT explorer](http://mqtt-explorer.com/) to monitor local eclipse-mosquitto topics/messages. And use test scripts from this Git repository to ensure the MQTT set up:

	`/mqtt/mqtt-listen.py or /mqtt/mqtt-test.py`

![MQTT Explorer](https://github.com/virshah24/azfn-edgemodule-mqtt-py/blob/master/media/azfunc-mqtt-explorer.PNG)

8. Finally, clone this Git repository and follow the [Microsoft Tutorial: Develop and deploy a Python IoT Edge module for Linux devices](https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-python-module) to deploy the Azure Function module on the edge. 

![VS Code - Python Azure Function](https://github.com/virshah24/azfn-edgemodule-mqtt-py/blob/master/media/azfunc-mqtt-vscode.png)