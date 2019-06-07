import random
import discord
from settings.config import FUN
import discord.ext.commands.errors as error
from discord.ext import commands

class Fun(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def praise(self, ctx):
    await ctx.send(':pray: All hail SnekLord! :pray:')  
    
  @commands.command()
  async def latency(self, ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms. Ambani does it better.')

  @commands.command()
  async def opinion(self, ctx, *, question):
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(FUN["responses"])}')

  @commands.command()
  async def spam(self, ctx, member: discord.Member, count, *, message="You have been warned."):
    '''Spam user from a server by mentioning them with no. of messages and a spam message.'''
    try:
      permissions = ctx.message.author.permissions_in(ctx.message.channel)
      if permissions.ban_members:
        for i in range(int(count)):
          await member.send(message)
        await ctx.channel.send(f'{member} spammed successfully.')
      else:
        await ctx.channel.send(f':x: You don\'t have the sufficient permissions {ctx.message.author.mention}.')
    except error.BadArgument:
      await ctx.channel.send(f':x: User {member} not found.')

def setup(client):
  client.add_cog(Fun(client))