import json

import twitchio
from twitchio.ext import commands

from .models import Channel, Message, User


class Bot(commands.Bot):

    def __init__(self, irc_token, username, channels):
        self.count = 0
        self.username = username
        self.channels = channels
        self.user = User.objects.get(username=username)
        self.colours = json.loads(self.user.colours)
        
        super().__init__(prefix=["c!!"], irc_token=irc_token,
                         nick=username, initial_channels=channels)

    async def event_ready(self):
        print("Bot ready")
        print(f"Username: {self.username}")
        print(f"Channels: {', '.join(self.channels)}")

    async def event_message(self, message):
        username = message.author.name
        if username != self.username:
            return

        colour = self.colours[self.count]
        msg = f"/color {colour}"
        try:
            await message.channel.colour(colour)
        except twitchio.errors.EchoMessageWarning:
            return

        channel = Channel.objects.get(username=message.channel)
        Message.objects.create(user=self.user, channel=channel, content=msg)
        try:
            last_time = self.user.message_set.all().order_by('-time')[9].time
        except IndexError:
            pass
        else:
            self.user.message_set.all().filter(time__lt=last_time).delete()

        if self.count == len(self.colours) - 1:
            self.count = 0
        else:
            self.count += 1

        await self.handle_commands(message)

    @commands.command(name="join_channels")
    async def join(self, ctx, *, channels):
        await self.join_channels(channels.split())

        self.channels.extend(channels.split())
        self.channels.sort()
