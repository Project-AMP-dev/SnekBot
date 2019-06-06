from client.base import client
from settings import config
import time
import discord
import discord.ext.commands.errors as error

@client.command()
async def clear(ctx, amount=config.COMMAND_CONFIG['clear_value']):
  await ctx.channel.purge(limit=(amount+1))
  await ctx.channel.send(f'Cleared {amount} messages.:boom:')
  time.sleep(2)
  await ctx.channel.purge(limit=1)
  
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.channel.send(f'Kicked {discord.Member} due to {reason}')


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.channel.send(f'Banned {discord.Member} due to {reason}')


@client.command()
async def warn(ctx, member: discord.Member, *, message="You have been warned."):
  try:
    await member.send(message)
    await ctx.channel.purge(limit=1)
  except error.BadArgument:
    await ctx.channel.send(f'User {member} not found.')
