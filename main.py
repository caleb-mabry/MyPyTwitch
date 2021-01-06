import asyncio

from settings import Settings
from twitchbot import TwitchBot

config = Settings()


event_loop = asyncio.get_event_loop()
TwitchBot(config, event_loop).run()
