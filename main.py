import logging
import sys

import asyncio
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
from qasync import QEventLoop

from core import setup_logger, Database
from windows import WindowManager

listening_started = False

if __name__ == "__main__":
    setup_logger()
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = WindowManager()
    window.show_summary()


    def start_listening():
        global listening_started
        if listening_started:
            logging.info("Подписка уже была запущена — пропускаем")
            return
        listening_started = True

        asyncio.create_task(
            Database.listen_channel("courier_is_registered", window.data_window.stop_timer)
        )
        asyncio.create_task(
            Database.listen_channel("order_status", window.summary_window.order_notify)
        )
        asyncio.create_task(
            Database.listen_channel("rate_delivery", window.summary_window.delivery_notify)
        )
        asyncio.create_task(
            Database.listen_channel("rating_changed", window.summary_window.courier_notify)
        )


    QTimer.singleShot(0, start_listening)

    with loop:
        loop.run_forever()
