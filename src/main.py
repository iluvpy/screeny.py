from PyQt5.QtWidgets import QApplication
from PIL import ImageGrab
import sys
import time
from program import Program

def main() -> int:
    app = QApplication(sys.argv)
    program = Program()
    program.start()

    exit_ = app.exec_()
    image_size = program.get_image_size()
    if image_size is not None:
        time.sleep(1) # wait for window to close
        image = ImageGrab.grab((image_size.x(), image_size.y(), image_size.width(), image_size.height()))
        image.save("screenshot.png")
    return exit_

if __name__ == "__main__":
    sys.exit(main())