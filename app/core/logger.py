# Auto-generated file
from app.mqtt.mqtt_client_base import MQTTClientBase
from app.core.logger import Logger
class MQTTClient(MQTTClientBase):
    def __init__(self, broker_address: str, broker_port: int, client_id: str):
        super().__init__(broker_address, broker_port, client_id)
        self.logger = Logger("MQTTClient")

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.logger.info("Connected to MQTT Broker!")
        else:
            self.logger.error(f"Failed to connect, return code {rc}")

    def on_disconnect(self, client, userdata, rc):
        self.logger.warning("Disconnected from MQTT Broker")

    def on_message(self, client, userdata, msg):
        self.logger.info(f"Received message: {msg.topic} -> {msg.payload.decode()}")

    def publish(self, topic: str, payload: str):
        result = self.client.publish(topic, payload)
        status = result[0]
        if status == 0:
            self.logger.info(f"Sent `{payload}` to topic `{topic}`")
        else:
            self.logger.error(f"Failed to send message to topic {topic}")
    
    def subscribe(self, topic: str):

        self.client.subscribe(topic)
        self.logger.info(f"Subscribed to topic `{topic}`")

    