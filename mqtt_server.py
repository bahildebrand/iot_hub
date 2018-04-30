import paho.mqtt.client as mqtt
import json
import datetime
from database import DataBase

db = None


def on_publish(mosquitto, object, message):
    pass


def on_message(mosquitto, object, message):
    print(message.payload)
    json_str = message.payload.decode('utf8').replace("'", '"')
    sensor_payload = json.loads(json_str)

    now = datetime.datetime.now()
    timestamp = {
        "timestamp": {
            "year": now.year,
            "month": now.month,
            "day": now.day,
            "hour": now.hour,
            "minute": now.minute
        }
    }

    sensor_payload.update(timestamp)

    db.push(message.topic, sensor_payload)

    # print(str(message.topic) + " " + str(message.qos) + " " +
    #       str(message.payload))

if __name__ == '__main__':
    config = json.load(open("config.json"))
    db = DataBase()

    client = mqtt.Client()
    client.on_message = on_message
    client.on_publish = on_publish

    client.connect(config["host_name"], 1883, 60)

    client.subscribe("#", 0)

    client.loop_forever()
