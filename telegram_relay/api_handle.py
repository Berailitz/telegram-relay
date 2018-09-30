"""define all apis under /api/"""
#!/usr/env/python3
# -*- coding: UTF-8 -*-

import logging
from flask_restful import Resource, Api, reqparse
from .bot_handler import BotHandler


bot_handler = BotHandler()


def create_api():
    """return api object at startup"""
    api = Api()
    api.add_resource(Relay, '/')
    return api


class Relay(Resource):
    def post(self):
        """edit method, return msg at /data/msg"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('text', type=str)
            raw_data = parser.parse_args()
            bot_handler.send_message(raw_data['text'])
            return {'status': 0, 'message': ''}
        except Exception as e:
            logging.exception(e)
            logging.error("Error sending message.")
            return {'status': 1, 'message': str(e.args)}
