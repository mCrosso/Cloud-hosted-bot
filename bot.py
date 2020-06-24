import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CheckFailure, has_role, command
import random
from random import randint
import datetime

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


#Avatar command
@client.command(aliases=['av', 'avatar', 'pfp'])
async def _av(ctx, user: discord.User = None):
    user = ctx.author if not user else user
    embed = discord.Embed(
        title=user.name,
        description='Avatar,',
        color=0xecce8b)
    pfp = user.avatar_url
    embed.set_image(url=pfp)
    await ctx.send(embed=embed)
#---------------------------------------------------------------------------------------------------------------------------------------------------

@client.command(aliases=['pp', 'ppsize'])
async def _ppsize(ctx, user: discord.User = None):
    user = ctx.author if not user else user
    colors = [0xFF0000, 0x000000, 0x0000FF, 0x008000, 0xFFFF00, 0xFFA500, 0x800080]
    randomchoice = random.choice(colors)
    value = random.randint(0, 15)
    embed = discord.Embed(
        title=user.name+"'s pp",
        description=('8'+ ('='*value)+ 'D'),
        color=randomchoice)
    await ctx.send(embed=embed)
#Id command
@client.command()
async def id(ctx, user: discord.User):
    await ctx.send(user.name)
#--------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def bigpp(ctx):
    user = ctx.author

    if user.id == 374321158700531712:
        await ctx.send(f'{user.name} has a small pp.')
    else:
        await ctx.send(f'{user.name} has a big pp.')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@client.event
async def on_message_delete(message):
    global deletedmessage
    deletedmessage = message.content

@client.command()
async def snipe(ctx):
    colors = [0xFF0000, 0x000000, 0x0000FF, 0x008000, 0xFFFF00, 0xFFA500, 0x800080]
    randomchoice = random.choice(colors)
    user = ctx.author
    embed = discord.Embed(
        title=user.name,
        description=(deletedmessage),
        timestamp=(datetime.datetime.utcnow()),
        color=randomchoice)
    await ctx.send(embed=embed)
client.run(os.environ['Discord_Token'])
