from settings.config import MODERATION
import asyncio
import discord
import discord.ext.commands.errors as error
from discord.ext import commands

class Moderation(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def clear(self, ctx, amount = MODERATION['default_clear_value']):
    '''Delete messages from a channel with the amount of messages specified.'''
    permissions = ctx.message.author.permissions_in(ctx.message.channel)
    if permissions.manage_messages:
      if amount < MODERATION['max_clear_value'] and amount > 0:
        await ctx.channel.purge(limit=(amount+1))
        await ctx.channel.send(f':white_check_mark: Cleared {amount} messages.:boom:')
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=1)
      else:
        await ctx.channel.send(f':x: Please make sure amount is between 0 and {MODERATION["max_clear_value"]}.') 
    else:
      await ctx.channel.send(f':x: You don\'t have the sufficient permissions {ctx.message.author.mention}.')

  @clear.error
  async def clear_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.channel.send(':x: Please enter a valid number.')
  
  @commands.command()
  async def kick(self, ctx, member : discord.Member, *, reason=MODERATION['default_kick_reason']):
    '''Kick user from a server by mentioning them with a reason.'''
    permissions = ctx.message.author.permissions_in(ctx.message.channel)
    if permissions.kick_members:
      await member.kick(reason=reason)
      await ctx.channel.send(f':white_check_mark: Kicked {member} due to {reason}')
    else:
      await ctx.channel.send(f':x: You don\'t have the sufficient permissions {ctx.message.author.mention}.')

  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.channel.send(':x: Please enter a valid user.')

  @commands.command()
  async def ban(self, ctx, member : discord.Member, *, reason=MODERATION['default_ban_reason']):
    '''Ban user from a server by mentioning them with a reason.'''
    permissions = ctx.message.author.permissions_in(ctx.message.channel)
    if permissions.ban_members: 
      await member.ban(reason=reason)
      await ctx.channel.send(f':white_check_mark: Banned {member} due to {reason}')
    else:
      await ctx.channel.send(f':x: You don\'t have the sufficient permissions {ctx.message.author.mention}.')
  
  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.channel.send(':x: Please enter a valid user.')

  @commands.command()
  async def warn(self, ctx, member: discord.Member, *, message="You have been warned."):
    '''Warn user from a server by mentioning them with a warning message.'''
    permissions = ctx.message.author.permissions_in(ctx.message.channel)
    if permissions.ban_members:
      await member.send(message)
      await ctx.channel.purge(limit=1)
      await ctx.channel.send(f'{member} warned successfully.')
    else:
      await ctx.channel.send(f':x: You don\'t have the sufficient permissions {ctx.message.author.mention}.')
    
  @warn.error
  async def warn_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.channel.send(':x: Please enter a valid user.')

  @commands.command()
  async def unban(self, ctx, *, member):
    '''Unban user from a server by mentioning them.'''
    permissions = ctx.message.author.permissions_in(ctx.message.channel)
    if permissions.ban_members:
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')

      for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
          await ctx.guild.unban(user)
          await ctx.channel.send(f':white_check_mark: Unbanned {user.mention}')
          return 
    else:
      await ctx.channel.send(f':x: You don\'t have the sufficient permissions {ctx.message.author.mention}.')

  @unban.error
  async def unban_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.channel.send(':x: Please enter a valid user.')

def setup(client):
  client.add_cog(Moderation(client))