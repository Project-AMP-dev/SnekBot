import discord
from discord.ext import commands
from commands.moderation import Moderation


class Error(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    '''
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.channel.send(':x: Please pass all required arguments.')
    if isinstance(error, commands.CommandNotFound):
      await ctx.channel.send(':x: Command Not Found!')
'''
def setup(client):
  client.add_cog(Error(client))