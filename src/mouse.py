
from PyQt5.QtCore import QPoint


class MouseButtons():
    left: int = 1
    right: int = 2

    @classmethod
    def is_left(cls, button: int) -> bool:
        return button == cls.left

    @classmethod
    def is_right(cls, button: int) -> bool:
        return button == cls.right

    @classmethod
    def is_button(cls, button: int) -> bool:
        return button == cls.left or button == cls.right

class MouseHandler:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.left = False
        self.rigt = False

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        
    def pos(self) -> QPoint:
        return QPoint(self.x, self.y)

    def btn_event(self, button: int, press_or_release: bool) -> None:
        if MouseButtons.is_left(button):
            self.left = press_or_release
        elif MouseButtons.is_right(button):
            self.right = press_or_release

    def press(self, button: int) -> None:
        self.btn_event(button, True) # True for press

    def release(self, button: int) -> None:
        self.btn_event(button, False) # False for release
    
    def left_down(self) -> bool:
        return self.left
    
    def right_down(self) -> bool:
        return self.right