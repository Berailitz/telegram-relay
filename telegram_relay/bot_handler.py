import logging
from .config import BOT_TOKEN, CHAT_IDS
from .queued_bot import create_queued_bot


class BotHandler(object):
    def __init__(self):
        self.bot = create_queued_bot(BOT_TOKEN)

    def send_message(self, text: str):
        """
        Send message."""
        logging.info(f"Send message: `{text}`")
        for chat_id in CHAT_IDS:
            self.bot.send_message(chat_id=chat_id, text=text)
