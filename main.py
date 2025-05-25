import sys

from PySide6.QtWidgets import QApplication

from windows.manager import WindowManager

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowManager()
    window.show_summary()
    sys.exit(app.exec())
