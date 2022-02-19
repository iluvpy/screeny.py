from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QRect, Qt, QEvent
from PyQt5.QtGui import QCloseEvent

from keys import KeyListener

class Program(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.keys = KeyListener()
        self.already_closed = False
        self.keys.listen()

        self.setWindowFlag(Qt.FramelessWindowHint) # remove title bar
        self.setGeometry(QRect(100, 100, 100, 100))
    

    def closeEvent(self, a0: QCloseEvent) -> None:
        print("closing")
        return super().closeEvent(a0)

    def event(self, event: QEvent) -> bool:
        if self.keys.is_pressed("esc") and not self.already_closed:
            self.already_closed = True
            self.close()
        
        return super().event(event)

    def start(self) -> None:
        self.showMaximized()