from PyQt5.QtWidgets import QApplication, QStackedWidget
import sys

from ui.welcome_screen import WelcomeScreen
from ui.verification_screen import VerificationScreen
from ui.qr_screen import QRScreen
from ui.connected_screen import ConnectedScreen
from ui.control_panel import ControlPanel

class UIManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.stack = QStackedWidget()

        self.screens = {
            "WELCOME": WelcomeScreen(),
            "VERIFY": VerificationScreen(),
            "QR": QRScreen(),
            "CONNECTED": ConnectedScreen(),
            "CONTROL": ControlPanel(),
        }

        for screen in self.screens.values():
            self.stack.addWidget(screen)

        self.stack.setFixedSize(800, 480)
        self.stack.show()

    def set_screen(self, state):
        self.stack.setCurrentWidget(self.screens[state])

    def run(self):
        sys.exit(self.app.exec_())