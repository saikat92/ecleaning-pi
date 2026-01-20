ecleaning-pi/
│
├── app/
│   ├── main.py                  # App entry point (state machine)
│   │
│   ├── config/
│   │   ├── device.json          # Device ID, version
│   │   ├── mqtt.json            # Broker, topics
│   │   └── wifi.json            # AP credentials
│   │
│   ├── core/
│   │   ├── state_manager.py     # Screen/state flow
│   │   ├── watchdog.py          # Safety & heartbeat
│   │   └── logger.py
│   │
│   ├── hardware/
│   │   ├── motor_controller.py  # Conveyor motors (2 motors)
│   │   ├── uv_controller.py     # UV lamp
│   │   ├── sensors.py           # Future expansion
│   │   └── gpio_map.py
│   │
│   ├── mqtt/
│   │   ├── mqtt_client.py       # Connect, publish, subscribe
│   │   └── topics.py            # Topic definitions
│   │
│   ├── network/
│   │   ├── wifi_ap.py           # Start hotspot
│   │   ├── qr_generator.py      # QR code with WiFi info
│   │   └── connection_check.py
│   │
│   ├── ui/
│   │   ├── welcome_screen.py
│   │   ├── verification_screen.py
│   │   ├── qr_screen.py
│   │   ├── connected_screen.py
│   │   └── control_panel.py
│   │
│   └── utils/
│       ├── constants.py
│       └── helpers.py
│
├── services/
│   └── ecleaning.service        # systemd auto-start
│
├── assets/
│   ├── logo.png
│   └── icons/
│
├── requirements.txt
├── README.md
└── scripts/
    ├── install.sh               # One-click setup
    └── reset_device.sh

