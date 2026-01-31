import json
import uuid
import ssl
import certifi

try:
    import paho.mqtt.client as mqtt
    MQTT_AVAILABLE = True
except ImportError:
    MQTT_AVAILABLE = False


class MQTTClient:
    BROKER = "test.mosquitto.org"
    PORT = 8883

    TOPIC_STATUS = "ecleaning/pi/status"
    TOPIC_COMMAND = "ecleaning/pi/command"

    def __init__(self, on_command_callback):
        self.on_command_callback = on_command_callback

        if MQTT_AVAILABLE:
            client_id = f"ecleaning-pi-{uuid.uuid4()}"
            self.client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv311)

            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.on_disconnect = self.on_disconnect
            
            self.client.tls_set(
                cert_reqs=ssl.CERT_NONE,
                tls_version=ssl.PROTOCOL_TLS_CLIENT
            )
            self.client.tls_insecure_set(True)

            self.client.connect(self.BROKER, self.PORT, 60)
            self.client.loop_start()
            
        else:
            print("[MQTT] Mock mode. UUID Not avialable.")

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("[MQTT] Connected successfully")
            client.subscribe(self.TOPIC_COMMAND)
        else:
            print("[MQTT] Connection failed, code:", rc)

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        print("[MQTT] Command received:", payload)
        self.on_command_callback(payload)

    def publish_status(self, state):
        message = json.dumps({"state": state})
        if MQTT_AVAILABLE:
            self.client.publish(self.TOPIC_STATUS, message)
        print("[MQTT] Status:", message)

    def on_disconnect(self, client, userdata, rc):
        print("[MQTT] Disconnected with code", rc)
