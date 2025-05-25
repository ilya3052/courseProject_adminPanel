class WindowManager:
    def __init__(self):
        from windows.reports import Reports
        from windows.summary import SummaryInfo

        self.reports_window = Reports(manager=self)
        self.summary_window = SummaryInfo(manager=self)

    def show_reports(self):
        self.summary_window.hide()
        self.reports_window.show()

    def show_summary(self):
        self.reports_window.hide()
        self.summary_window.show()