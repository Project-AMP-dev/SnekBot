import discord
from discord.ext import commands, tasks
from itertools import cycle
from settings.config import EVENTS

class GeneralEvents(commands.Cog):
  
  def __init__(self, client):
    self.client = client
    self.status = cycle(EVENTS['status'])

  @commands.Cog.listener()
  async def on_ready(self):
    self.change_status.start()
    print('Bot is ready.')

  @commands.Cog.listener()
  async def on_member_join(self, member):
    print(f'{member} has joined a server.')

  @commands.Cog.listener()
  async def on_member_remove(self, member):
    print(f'{member} has left the server.')

  @tasks.loop(minutes=5)
  async def change_status(self):
    await self.client.change_presence(status = discord.Status.idle, activity = discord.Game(next(self.status)))

def setup(client):
  client.add_cog(GeneralEvents(client))