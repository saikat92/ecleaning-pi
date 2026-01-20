import time

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO_AVAILABLE = True
except ImportError:
    GPIO_AVAILABLE = False

class HardwareController:
    # GPIO pin mapping (BCM)
    MOTOR_PIN = 17
    UV_LAMP_PIN = 27
    BUZZER_PIN = 22
    INDICATOR_LED_PIN = 13
    EMERGENCY_PIN = 5  # Physical emergency switch

    def __init__(self):
        if GPIO_AVAILABLE:
            GPIO.setup(self.MOTOR_PIN, GPIO.OUT)
            GPIO.setup(self.UV_LAMP_PIN, GPIO.OUT)
            GPIO.setup(self.BUZZER_PIN, GPIO.OUT)
            self.all_off()

    def motor_on(self):
        if GPIO_AVAILABLE:
            GPIO.output(self.MOTOR_PIN, GPIO.HIGH)
        print("[HW] Motor ON")

    def motor_off(self):
        if GPIO_AVAILABLE:
            GPIO.output(self.MOTOR_PIN, GPIO.LOW)
        print("[HW] Motor OFF")

    def uv_on(self):
        if GPIO_AVAILABLE:
            GPIO.output(self.UV_LAMP_PIN, GPIO.HIGH)
        print("[HW] UV Lamp ON")

    def uv_off(self):
        if GPIO_AVAILABLE:
            GPIO.output(self.UV_LAMP_PIN, GPIO.LOW)
        print("[HW] UV Lamp OFF")

    def beep(self, duration=0.2):
        if GPIO_AVAILABLE:
            GPIO.output(self.BUZZER_PIN, GPIO.HIGH)
            time.sleep(duration)
            GPIO.output(self.BUZZER_PIN, GPIO.LOW)
        print("[HW] Beep")
    
    def indicator(self, duration=0.2):
        if GPIO_AVAILABLE:
            GPIO.output(self.INDICATOR_LED_PIN, GPIO.HIGH)
            time.sleep(duration)
            GPIO.output(self.INDICATOR_LED_PIN, GPIO.LOW)
        print("[HW] Indicator LED Blink")

    def all_off(self):
        if GPIO_AVAILABLE:
            GPIO.output(self.MOTOR_PIN, GPIO.LOW)
            GPIO.output(self.UV_LAMP_PIN, GPIO.LOW)
            GPIO.output(self.BUZZER_PIN, GPIO.LOW)

    def cleanup(self):
        if GPIO_AVAILABLE:
            GPIO.cleanup()
    
    def __init__(self):
        if GPIO_AVAILABLE:
            GPIO.setup(self.EMERGENCY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(
                self.EMERGENCY_PIN,
                GPIO.FALLING,
                callback=self.emergency_triggered,
                bouncetime=300
            )

    def emergency_triggered(self, channel):
        print("[HW] EMERGENCY STOP TRIGGERED")
        self.all_off()