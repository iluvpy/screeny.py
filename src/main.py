from pynput import mouse
from ClearWindow import ClearWindow
import time
import threading

class Mouse:
    pressed = False
    position = [0, 0]

    @classmethod
    def press(cls):
        cls.pressed = True

    @classmethod
    def release(cls):
        cls.pressed = False

    @classmethod
    def on_move(cls, x, y):
        cls.position = [x, y]

    @classmethod
    def on_click(cls, x, y, button, pressed):
        cls.pressed = pressed
        cls.position = [x, y]

def main() -> None:

    mouse_listener = mouse.Listener(
        on_move=Mouse.on_move,
        on_click=Mouse.on_click)
    mouse_listener.start()
     
    window = ClearWindow(100, 100)
    window_thread = threading.Thread(target=window.open)
    window_thread.start()

    while True:
        print(Mouse.position)
        time.sleep(0.1)

if __name__ == "__main__":
    main()