import random
from client.base import client

@client.command()
async def praise(ctx):
  await ctx.send(':pray: All hail SnekLord! :pray:')  
  
@client.command()
async def latency(ctx):
  await ctx.send(f'{round(client.latency * 1000)}ms. Ambani does it better.')

@client.command(aliases=['8ball','opinion'])
async def _8ball(ctx, *, question):
  responses = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes - definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    'Don\'t count on it.',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
  ]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')