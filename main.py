import asyncio

from bot.settings import Settings
from bot.twitchbot import TwitchBot


config = Settings()

event_loop = asyncio.get_event_loop()
TwitchBot(config, event_loop).run()
