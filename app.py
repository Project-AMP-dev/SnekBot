import discord
import os
from pyfiglet import figlet_format
from settings import config
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

print(figlet_format("Snek\nBot", font = "slant" ))


@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./commands'):
  if filename.endswith('.py'):
    client.load_extension(f'commands.{filename[:-3]}')

for filename in os.listdir('./events'):
  if filename.endswith('.py'):
    client.load_extension(f'events.{filename[:-3]}')

Token = config.DISCORD['token']
client.run(Token)