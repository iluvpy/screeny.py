from PyQt5.QtWidgets import QApplication
import sys
from program import Program



def main() -> None:
    app = QApplication(sys.argv)
    program = Program()
    program.start()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()