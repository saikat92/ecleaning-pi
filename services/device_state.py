class DeviceState:
    IDLE = "Idle"
    MACHINE_ON = "Machine On"
    AUTO_CLEANING = "Automatic Cleaning Mode selected"
    MANUAL_CLEANING = "Manual Cleaning Mode selected"
    UV_ON = "UV Light Turned On"
    UV_OFF = "UV Light Turned Off"
    CONV_ON = "Conveyor Running.."
    CONV_OFF = "Conveyor Stopped"
    PAUSED = "paused"
    ERROR = "error"
    CALLIBRATE = "Checking System..."
    RESTART = "Restarting system..."
    CLEANING_START = "Cleaning Started"
    CLEANING_COMPLETE = "Cleaning completes. Collect Packet"

    def __init__(self):
        self.state = self.IDLE

    def set_state(self, new_state):
        print(f"[STATE] {self.state} → {new_state}")
        self.state = new_state

    def get_state(self):
        return self.state
