class DeviceState:
    IDLE = "idle"
    CLEANING = "cleaning"
    PAUSED = "paused"
    ERROR = "error"

    def __init__(self):
        self.state = self.IDLE

    def set_state(self, new_state):
        print(f"[STATE] {self.state} → {new_state}")
        self.state = new_state

    def get_state(self):
        return self.state
