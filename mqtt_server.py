import paho.mqtt.client as mqtt
import json

def on_publish(mosquitto, object, message):
    pass

def on_message(mosquitto, object, message):
    print(str(message.topic) + " " + str(message.qos) + " " + str(message.payload))

if __name__ == '__main__':
    config = json.load(open("config.json"))

    client = mqtt.Client()
    client.on_message = on_message
    client.on_publish = on_publish

    client.connect(config["host_name"], 1883, 60)

    client.subscribe("test/#", 0)

    client.loop_forever()