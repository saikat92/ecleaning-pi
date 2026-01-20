from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class VerificationScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Running system verification...Motors • UV • Safety")
        label.setStyleSheet("font-size: 24px;")
        layout.addWidget(label)
        self.setLayout(layout)