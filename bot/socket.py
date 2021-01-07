import aiohttp
import logging

from aiohttp.client_ws import ClientWebSocketResponse

from bot.settings import Settings
from bot.variablemappings.settingsFields import SettingsFields
from bot.server_response_handler import ServerResponseHandler

WEB_SOCKET_SSL = 'wss://irc-ws.chat.twitch.tv:443'

class Socket:
    def __init__(self, config: Settings):
        self.ws = None
        self._config = config

    async def connect(self):
        session = aiohttp.ClientSession()
        self.ws = await session.ws_connect(WEB_SOCKET_SSL)
        await self.ws.send_str(f'PASS {self._config.settings.get(SettingsFields.OAUTH_TOKEN.value)}')
        await self.ws.send_str(f'NICK {self._config.settings.get(SettingsFields.BOT_NICKNAME.value)}')
        await self.ws.send_str(f'JOIN #{self._config.settings.get(SettingsFields.CHANNEL_NAME.value)}')

    async def listen(self):
        while True:
            if self.ws is None:
                logging.info('connecting...')
                await self.connect()
            socket_response = await self.ws.receive_str()
            await ServerResponseHandler.handle_message(socket_response, self.ws)
            # await self._msg_handler.handle_message(await self._ws.receive_str())

    async def send_message(self, response: str):
        await self.ws.send_str(response)

    