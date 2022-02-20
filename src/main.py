from PyQt5.QtWidgets import QApplication
from PIL import ImageGrab
from pynput import keyboard
import sys
import time
from program import ScrenshotProgram, ExitMethod

def main() -> int:
    
    def on_press(key):
        if key == keyboard.Key.f12:
            return False
        return True

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    app = QApplication(sys.argv)
    program = ScrenshotProgram()
    program.start()

    exit_ = app.exec_()
    image_size = program.get_image_size()
    if image_size is not None: # if an image was taken
        time.sleep(1) # wait for window to close
        image = ImageGrab.grab((image_size.x(), image_size.y(), image_size.width(), image_size.height()))
        image.save("screenshot.png")

    if program.get_exit_method() == ExitMethod.UKNOWN:
        return exit_ # didnt exit normally (ie. escape or by taking an image)
    else:
        return main() # restart listener to take another screenshot

if __name__ == "__main__":
    sys.exit(main())