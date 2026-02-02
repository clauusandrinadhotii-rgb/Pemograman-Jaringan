import time
import psutil
import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPIC = "sensor/cpu"

print("Agent hidup...")

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    cpu = psutil.cpu_percent()
    data = {
        "device": "agent-1",
        "cpu": cpu
    }
    client.publish(TOPIC, json.dumps(data))
    print("Kirim data:", data)
    time.sleep(2)