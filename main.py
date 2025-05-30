import sys

import asyncio
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
from qasync import QEventLoop

from core import setup_logger, Database
from windows import WindowManager


if __name__ == "__main__":
    setup_logger()
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = WindowManager()
    window.show_summary()

    # Запускаем асинхронную задачу после старта event loop
    def start_listening():
        asyncio.create_task(
            Database.listen_channel("courier_is_registered", window.data_window.stop_timer)
        )

    QTimer.singleShot(0, start_listening)

    with loop:
        loop.run_forever()
