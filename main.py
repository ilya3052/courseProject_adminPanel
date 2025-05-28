import sys

from PySide6.QtWidgets import QApplication

from core import setup_logger
from windows import WindowManager

if __name__ == "__main__":
    setup_logger()
    app = QApplication(sys.argv)
    window = WindowManager()
    window.show_summary()
    sys.exit(app.exec())
