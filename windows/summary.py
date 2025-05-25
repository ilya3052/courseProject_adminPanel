import sys

from PySide6.QtWidgets import QMainWindow

from windows_design import SummaryWindow


class SummaryInfo(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self._ui = SummaryWindow()
        self._ui.setupUi(self)
        self.setup_actions()

    def setup_actions(self):
        self._ui.reports.triggered.connect(self.manager.show_reports)

