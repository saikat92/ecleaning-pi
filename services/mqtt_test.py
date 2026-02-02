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
            device.set_state(DeviceState.MACHINE_ON)
        elif action == "pause":
            device.set_state(DeviceState.PAUSED)
        elif action == "stop":
            device.set_state(DeviceState.IDLE)
        elif action == "auto_clean":
            device.set_state(DeviceState.AUTO_CLEANING)
        elif action == "man_clean":
            device.set_state(DeviceState.MANUAL_CLEANING)
        elif action == "uv_on":
            device.set_state(DeviceState.UV_ON)
        elif action == "uv_off":
            device.set_state(DeviceState.UV_OFF)
        elif action == "conv_on":
            device.set_state(DeviceState.CONV_ON)
        elif action == "conv_off":
            device.set_state(DeviceState.CONV_OFF)
        elif action == "calibrate":
            device.set_state(DeviceState.CALLIBRATE)
        elif action == "restart":
            device.set_state(DeviceState.RESTART)
        elif action == "clean_start":
            device.set_state(DeviceState.CLEANING_START)
        
        else:
            print("[APP] Unknown command:", action)

    except Exception as e:
        print("[APP] Command error:", e)

mqtt = MQTTClient(on_command)

while True:
    mqtt.publish_status(device.get_state())
    time.sleep(5)
