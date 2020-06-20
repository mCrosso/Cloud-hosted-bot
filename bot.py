import discord
import os
from discord.ext import commands
import random


client = commands.Bot(command_prefix='.')
@client.event
async def on_ready():
    print('Bot is running.')

#Ping command
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! Ping is {round(client.latency * 1000)}ms")
#---------------------------------------------------------------------------------------------------------------------------------------------------------




#8ball command
@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx):
    responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes – definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.',
'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.',
'Concentrate and ask again.', "Don't count on it.", 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
    await ctx.send(random.choice(responses))
#---------------------------------------------------------------------------------------------------------------------------------------------------
#fun command
@client.command()
async def isbuttergay(ctx):
    await ctx.send('OFC SHE IS!')
#---------------------------------------------------------------------------------------------------------------------------------------------------

#the say command
@client.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)
#---------------------------------------------------------------------------------------------------------------------------------------------------


#purge command
@client.command(aliases=['clear', 'purge'])
async def _purge(ctx, amount=15):
    if ctx.author == client:
        return
    await ctx.message.delete(delay=None)
    await ctx.channel.purge(limit=amount)

#---------------------------------------------------------------------------------------------------------------------------------------------------

client.run('NzIyNTgyNTYzNDM2MTAxNjgz.XulTZQ.mgLKd6dq9mJ6jMAgdUG5vYgiVC8')
