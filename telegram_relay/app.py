"""main module including create_app()"""
#!/usr/env/python3
# -*- coding: UTF-8 -*-

import logging
import os
from flask import Flask
from .api_handle import create_api
from .mess import get_current_time, set_logger
try:
    from .config import IS_DEBUG
except ImportError as config_import_error:
    print(config_import_error.args)
    raise ImportError(
        "Failed to import configs. Please make sure `config.py` exists.")


def create_app(log_path='log'):
    """create initialized flask app, compatible with uwsgi"""
    if not os.path.exists(log_path):
        raise FileNotFoundError(f'Log path does not exist: `{log_path}`.')
    set_logger(
        f'{log_path}/telegram_relay_{get_current_time()}_{os.getpid()}.log')
    app = Flask(__name__)
    api = create_api()
    api.init_app(app)
    logging.info('%r', app.view_functions)
    logging.info('%r', app.url_map)
    return app
