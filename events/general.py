from client.base import client
@client.event
async def on_ready():
  print('Bot is ready.')

@client.event
async def on_member_join(ctx, member):
  ctx (f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
  print(f'{member} has left the server.')