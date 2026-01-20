from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap

class QRScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Scan QR to connect")
        qr = QLabel()
        qr.setPixmap(QPixmap("assets/qr.png").scaled(250, 250))
        layout.addWidget(label)
        layout.addWidget(qr)
        self.setLayout(layout)