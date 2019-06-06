from client.base import client
from settings import config
import time
import discord
import discord.ext.commands.errors as error

@client.command()
async def clear(ctx, amount=config.COMMAND_CONFIG['default_clear_value']):
  try:
    if amount < config.COMMAND_CONFIG['max_clear_value'] and amount > 0:
      await ctx.channel.purge(limit=(amount+1))
      await ctx.channel.send(f'Cleared {amount} messages.:boom:')
      time.sleep(2)
      await ctx.channel.purge(limit=1)
    else:
      await ctx.channel.send(f':warning:Please make sure amount is between 0 and {config.COMMAND_CONFIG["max_clear_value"]}.') 
  except error.BadArgument:
    await ctx.channel.send(f':warning:Not a valid number.')
  
@client.command()
async def kick(ctx, member : discord.Member, *, reason="Unknown reason.:shrug:"):
  try:
    if ctx.message.author.s
      kick_user = discord.Member
      await member.kick(reason=reason)
      await ctx.channel.send(f'Kicked {kick_user} due to {reason}')
    else:
      await ctx.channel.send(f'You don\'t have the permissions {ctx.message.author.name}.')
  except error.BadArgument:
    await ctx.channel.send(f':warning:User not found. ')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  try:
    ban_user = discord.Member 
    await member.ban(reason=reason)
    await ctx.channel.send(f'Banned {ban_user} due to {reason}')
  except error.CommandInvokeError:
    await ctx.channel.send()

@client.command()
async def warn(ctx, member: discord.Member, *, message="You have been warned."):
  try:
    await member.send(message)
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(f'{member} warned successfully.')
  except error.BadArgument:
    await ctx.channel.send(f'User {member} not found.')

@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.channel.send(f'Unbanned {user.mention}')
      return 