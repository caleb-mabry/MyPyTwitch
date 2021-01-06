import aiohttp
import asyncio

from settings import Settings
from enumerations.settingsFields import SettingsFields
WEB_SOCKET_SSL = 'wss://irc-ws.chat.twitch.tv:443'


class TwitchBot():
    def __init__(self, config: Settings, event_loop: asyncio.AbstractEventLoop):
        self._ws = None
        self._loop = event_loop
        self._config = config

    async def connect(self):
        session = aiohttp.ClientSession()
        self._ws = await session.ws_connect(WEB_SOCKET_SSL)
        await self._ws.send_str(f'PASS {self._config.settings.get(SettingsFields.OAUTH_TOKEN.value)}')
        await self._ws.send_str(f'NICK {self._config.settings.get(SettingsFields.BOT_NICKNAME.value)}')
        await self._ws.send_str(f'JOIN #{self._config.settings.get(SettingsFields.CHANNEL_NAME.value)}')

    async def listen(self):
        while True:
            if self._ws is None:
                print('connecting...')
                await self.connect()
            print(await self._ws.receive())

    def run(self):
        self._loop.run_until_complete(self.connect())

        try:
            self._loop.run_until_complete(self.listen())
        except KeyboardInterrupt as e:
            pass
