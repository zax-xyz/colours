import asyncio

from celery.decorators import task

from . import bot as colours_bot

@task(name="run_bot")
def run_bot(irc_token, username, channels):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    bot = colours_bot.Bot(irc_token, username, channels)
    loop.run_until_complete(bot.run())
