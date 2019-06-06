from client.base import client
from settings import config
import time


@client.command()
async def clear(ctx, amount=config.COMMAND_CONFIG['clear_value']):
  await ctx.channel.purge(limit=(amount+1))
  await ctx.channel.send(f'Cleared {amount} messages.:boom:')
  time.sleep(2)
  await ctx.channel.purge(limit=1)
  
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)