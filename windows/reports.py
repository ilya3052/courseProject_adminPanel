from PySide6.QtWidgets import QMainWindow

from windows_design import ReportsWindow


class Reports(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self._ui = ReportsWindow()
        self._ui.setupUi(self)
        self.setup_actions()

    def setup_actions(self):
        self._ui.summary.triggered.connect(self.manager.show_summary)

