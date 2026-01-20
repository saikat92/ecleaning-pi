# ================================
# core/state_manager.py
# Central state machine controlling UI + system flow
# ================================

from sre_parse import State
import time
from services.hardware_controller import HardwareController
from services.mqtt_client import MQTTClient
from ui.ui_manager import UIManager
from network.wifi_ap import start_hotspot
from network.qr_generator import generate_qr
from network.connection_check import android_connected

class StateManager:
    def __init__(self):
        self.current_state = "WELCOME"
        self.state_start_time = time.time()
        self.hw = HardwareController()
        self.mqtt = MQTTClient(self.handle_mqtt_command)
        self.mqtt.publish_status(self.state.name)
        self.ui = UIManager()
        self.fault_reason = None

    def set_state(self, new_state):
        print(f"[STATE] {self.current_state} -> {new_state}")
        self.current_state = new_state
        self.state_start_time = time.time()
        self.ui.set_screen(new_state)

    def run(self):
        if self.current_state == "WELCOME":
            self.welcome_state()

        elif self.current_state == "VERIFY":
            self.verification_state()

        elif self.current_state == "QR":
            self.qr_state()

        elif self.current_state == "CONNECTED":
            self.connected_state()

        elif self.current_state == "CONTROL":
            self.control_state()
            self.hw.motor_on()
            self.hw.uv_on()

        elif self.state == State.CONNECTED:
            self.hw.beep()
            self.hw.indicator()

        elif self.current_state == "EMERGENCY_STOP":
            self.emergency_state()

        elif self.current_state == "FAULT":
            self.fault_state()  

    def handle_mqtt_command(self, command):
        if command == "CONNECT":
            self.state = State.CONNECTED
        elif command == "START":
            self.state = State.CONTROL
        elif command == "STOP":
            self.state = State.WELCOME
        elif command == "EMERGENCY_STOP":
            self.enter_emergency()
        
    def enter_emergency(self):
        self.hw.all_off()
        self.set_state("EMERGENCY_STOP")

    def enter_fault(self, reason):
        self.fault_reason = reason
        self.hw.all_off()
        self.set_state("FAULT")

    def emergency_state(self):
        self.hw.all_off()
        # Wait for manual reset
        pass    
    
    def fault_state(self):
        print(f"[FAULT] {self.fault_reason}")
        self.hw.all_off()
    # ---------------- STATES ----------------

    def welcome_state(self):
        # Show logo screen
        if self.elapsed(3):
            self.set_state("VERIFY")

    def verification_state(self):
        # Placeholder for motor + UV checks
        print("Running system verification...")
        time.sleep(2)
        self.set_state("QR")

    def qr_state(self):
        start_hotspot()
        generate_qr()
        print("Waiting for Android connection...")
        if android_connected():
            self.set_state("CONNECTED")

    def connected_state(self):
        # Brief success screen
        if self.elapsed(2):
            self.set_state("CONTROL")

    def control_state(self):
        # Main operational state
        pass
    
    def shutdown(self):
        self.hw.all_off()
        self.hw.cleanup()
        print("Hardware controller cleaned up.")
    # ---------------- HELPERS ----------------

    def elapsed(self, seconds):
        return (time.time() - self.state_start_time) >= seconds

    def shutdown(self):
        print("Shutting down state manager safely...")

