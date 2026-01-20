from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        start = QPushButton("Start Cleaning")
        stop = QPushButton("Stop")
        emergency = QPushButton("Emergency Stop")

        start.setStyleSheet("font-size: 22px;")
        stop.setStyleSheet("font-size: 22px;")
        emergency.setStyleSheet("font-size: 22px; background:red; color:white;")

        layout.addWidget(start)
        layout.addWidget(stop)
        layout.addWidget(emergency)
        self.setLayout(layout)