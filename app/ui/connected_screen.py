from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class ConnectedScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Device Connected Successfully")
        label.setStyleSheet("font-size: 26px; color: green;")
        layout.addWidget(label)
        self.setLayout(layout)