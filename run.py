"""start main app"""
#!/usr/env/python3
# -*- coding: UTF-8 -*-

import logging
import os
from pathlib import Path
from telegram_relay.app import create_app
from telegram_relay.config import IS_DEBUG, LOG_FLODER, WEB_PORT
from telegram_relay.mess import set_logger

application = create_app(log_path='log')


def main():
    """main func"""
    log_path = Path(LOG_FLODER, f'LibraryMonitor_{os.getpid()}.log')
    if not log_path.parent.exists():
        log_path.parent.mkdir(parents=True)
    set_logger(log_path)
    application.run(port=WEB_PORT, debug=IS_DEBUG)
    logging.warning("TelegramRelay: Exits.")


if __name__ == '__main__':
    main()
