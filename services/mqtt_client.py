import json
import time

try:
    import paho.mqtt.client as mqtt
    MQTT_AVAILABLE = True
except ImportError:
    MQTT_AVAILABLE = False

class MQTTClient:
    BROKER = "broker.hivemq.com"  # public broker for demo
    PORT = 1883
    TOPIC_STATUS = "ecleaning/pi/status"
    TOPIC_COMMAND = "ecleaning/pi/command"

    def __init__(self, on_command_callback):
        self.on_command_callback = on_command_callback
        if MQTT_AVAILABLE:
            self.client = mqtt.Client()
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.connect(self.BROKER, self.PORT, 60)
            self.client.loop_start()
        else:
            print("[MQTT] Running in mock mode")

    def on_connect(self, client, userdata, flags, rc):
        print("[MQTT] Connected with result code", rc)
        client.subscribe(self.TOPIC_COMMAND)

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        print("[MQTT] Command received:", payload)
        self.on_command_callback(payload)

    def publish_status(self, state):
        message = json.dumps({"state": state})
        if MQTT_AVAILABLE:
            self.client.publish(self.TOPIC_STATUS, message)
        print("[MQTT] Status published:", message)