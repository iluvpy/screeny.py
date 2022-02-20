from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QEvent, QRect
from PyQt5.QtGui import QCloseEvent, QKeyEvent, QMouseEvent, QPaintEvent, QPainter, QPen
from keys import KeyHandler
from mouse import MouseHandler
from enum import Enum, auto

class ExitMethod:
    IMAGE_TAKEN = auto()
    ESCAPE = auto()
    UKNOWN = auto()

class ScrenshotProgram(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.mouse = MouseHandler()
        self.keys = KeyHandler()
        self.exit_method = ExitMethod.UKNOWN
        self.already_closed = False
        self.last_down_pos = None
        self.image_size = None
        self.init_window()
        
    

    def init_window(self):
        # here i set all the window attributes
        self.setWindowFlag(Qt.FramelessWindowHint) # remove title bar
        self.setWindowOpacity(0.5)
        self.setWindowTitle("Screeny.py")

    def closeEvent(self, event: QCloseEvent) -> None:
        if not self.already_closed:
            self.already_closed = True
            print("closing screenshot taker...")
            return super().closeEvent(event)

    def event(self, event: QEvent) -> bool:
        if self.keys.is_pressed(Qt.Key.Key_Escape) and not self.already_closed:
            self.exit_method = ExitMethod.ESCAPE
            self.close()
        
        if self.mouse.left_down() and self.last_down_pos is None:
            self.last_down_pos = self.mouse.pos()
            print(f"{self.last_down_pos.x()}x {self.last_down_pos.y()}y")
        
        if not self.mouse.left_down() and self.last_down_pos is not None:
            release_point = self.mouse.pos()
            x = self.last_down_pos.x()
            y = self.last_down_pos.y()
            rx = release_point.x()
            ry = release_point.y()
            
            if x > rx: rx, x = x, rx
            if y > ry: ry, y = y, ry

            self.image_size = QRect(x, y, rx, ry)
            self.exit_method = ExitMethod.IMAGE_TAKEN
            self.close()
        
        self.update()
        return super().event(event)


    def paintEvent(self, paint_event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))
        if self.last_down_pos is not None:
            mouse_pos = self.mouse.pos()
            x = self.last_down_pos.x()
            y = self.last_down_pos.y()
            x2 = mouse_pos.x()
            y2 = mouse_pos.y()
            painter.drawRect(QRect(x, y, x2-x, y2-y)) 
        
        return super().paintEvent(paint_event)

    def keyPressEvent(self, key_event: QKeyEvent) -> None:
        self.keys.press(key_event.key())
        return super().keyPressEvent(key_event)

    def keyReleaseEvent(self, key_event: QKeyEvent) -> None:
        self.keys.release(key_event.key())
        return super().keyReleaseEvent(key_event)

    def mousePressEvent(self, mouse_event: QMouseEvent) -> None:
        self.mouse.move(mouse_event.x(), mouse_event.y())
        self.mouse.press(mouse_event.button())
        return super().mousePressEvent(mouse_event)

    def mouseReleaseEvent(self, mouse_event: QMouseEvent) -> None:
        self.mouse.move(mouse_event.x(), mouse_event.y())
        self.mouse.release(mouse_event.button())
        return super().mousePressEvent(mouse_event)

    def mouseMoveEvent(self, mouse_event: QMouseEvent) -> None:
        self.mouse.move(mouse_event.x(), mouse_event.y())
        return super().mouseMoveEvent(mouse_event)

    def start(self) -> None:
        self.showFullScreen()
    
    def get_image_size(self) -> QRect:
        return self.image_size

    def get_exit_method(self) -> ExitMethod:
        return self.exit_method