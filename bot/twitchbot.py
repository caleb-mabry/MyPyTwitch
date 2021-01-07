import asyncio
import logging

from bot.socket import Socket


class TwitchBot():
    def __init__(self, socket: Socket, event_loop: asyncio.AbstractEventLoop):
        self._ws = socket
        self._loop = event_loop

    def run(self):
        self._loop.run_until_complete(self._ws.connect())
        try:
            self._loop.run_until_complete(self._ws.listen())
        except KeyboardInterrupt as e:
            logging.error(e)
            pass
