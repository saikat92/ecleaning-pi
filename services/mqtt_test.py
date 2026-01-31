from mqtt_client import MQTTClient
from device_state import DeviceState
import json
import time

device = DeviceState()

def on_command(cmd):
    try:
        data = json.loads(cmd)
        action = data.get("action")

        if action == "start":
            device.set_state(DeviceState.CLEANING)
        elif action == "pause":
            device.set_state(DeviceState.PAUSED)
        elif action == "stop":
            device.set_state(DeviceState.IDLE)
        else:
            print("[APP] Unknown command:", action)

    except Exception as e:
        print("[APP] Command error:", e)

mqtt = MQTTClient(on_command)

while True:
    mqtt.publish_status(device.get_state())
    time.sleep(5)
