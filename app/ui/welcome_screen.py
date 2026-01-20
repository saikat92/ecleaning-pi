from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        logo = QLabel()
        logo.setPixmap(QPixmap("assets/logo.png").scaled(300, 300, Qt.KeepAspectRatio))
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)
        self.setLayout(layout)