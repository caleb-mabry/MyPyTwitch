import asyncio

from bot.settings import Settings
from bot.twitchbot import TwitchBot
from bot.socket import Socket

config = Settings()
web_socket = Socket(config)
event_loop = asyncio.get_event_loop()
TwitchBot(web_socket, event_loop).run()
