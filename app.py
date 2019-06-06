import discord
import commands
import events

from pyfiglet import figlet_format
from settings import config
from client.base import client

print(figlet_format("Snek\nBot", font = "slant" ))


Token = config.DISCORD_CONFIG['token']

client.run(Token)