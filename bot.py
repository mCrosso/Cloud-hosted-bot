import datetime
import random

import discord
from discord.ext import commands
import sqlite3

client = commands.Bot(command_prefix='.')
client.remove_command('help')


@client.event
async def on_ready():
    print('Bot is running.')
#-------------------------------------------------------------------------------------------------------------------
@client.command()
async def createacc(ctx):
    name = ctx.author
    name2 = f"'{name.id}'"
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    sql = (f'INSERT INTO main (username, balance)'
           f'VALUES(({name2}), (0))')
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    await ctx.send('Account made!')
@createacc.error
async def on_error(ctx, error):
    await ctx.send('You already have an account.')
@client.command()
async def bal(ctx):
    user = ctx.author
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute(f"SELECT balance FROM main WHERE username = '{ctx.author.id}'")
    result = cursor.fetchone()
    amount = str(result[0])
    embed = discord.Embed(
        description=f'You have {amount} coins.',
        color=0x000000)
    embed.set_author(name=f"{user.name}'s balance", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
@client.command()
async def work(ctx):
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    sql = (f"UPDATE main SET balance = (balance + 5) WHERE username = '{ctx.author.id}'")
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    await ctx.send('You worked for an hour and got 5 coins!')

#-----------------------------------------------------------------------------------------------------------------------
# Ping command
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! Ping is {round(client.latency * 1000)}ms")



@client.command()
async def testtest(ctx, message):
    num = 1
    while num == 1:
        await ctx.send(message)
# ---------------------------------------------------------------------------------------------------------


# 8ball command
@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx):
    responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes – definitely.',
                 'You may rely on it.', 'As I see it, yes.', 'Most likely.',
                 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.',
                 'Better not tell you now.', 'Cannot predict now.',
                 'Concentrate and ask again.', "Don't count on it.", 'My reply is no.', 'My sources say no.',
                 'Outlook not so good.', 'Very doubtful.']
    await ctx.send(random.choice(responses))


# ---------------------------------------------------------------------------------------------------------------------------------------------------
# fun command
@client.command()
async def isbuttergay(ctx):
    await ctx.send('OFC SHE IS!')


# ---------------------------------------------------------------------------------------------------------------------------------------------------

# the say command
@client.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)


# ---------------------------------------------------------------------------------------------------------------------------------------------------


# purge command
@client.command(aliases=['clear', 'purge'])
async def _purge(ctx, amount=15):
    if ctx.author == client:
        return
    await ctx.message.delete(delay=None)
    await ctx.channel.purge(limit=amount)


# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Avatar command
@client.command(aliases=['av', 'avatar', 'pfp'])
async def _av(ctx, user: discord.User = None):
    user = ctx.author if not user else user
    embed = discord.Embed(
        description='Avatar',
        color=0xecce8b)
    pfp = user.avatar_url
    embed.set_author(name=user.name, icon_url=ctx.author.avatar_url)
    embed.set_image(url=pfp)
    await ctx.send(embed=embed)


# ---------------------------------------------------------------------------------------------------------------------------------------------------

# pp size command
@client.command(aliases=['pp', 'ppsize'])
async def _ppsize(ctx, user: discord.User = None):
    user = ctx.author if not user else user
    colors = [0xFF0000, 0x000000, 0x0000FF, 0x008000, 0xFFFF00, 0xFFA500, 0x800080]
    randomchoice = random.choice(colors)
    value = random.randint(0, 15)
    embed = discord.Embed(
        title=user.name + "'s pp",
        description=('8' + ('=' * value) + 'D'),
        color=randomchoice)
    await ctx.send(embed=embed)
    global deschelp
    deschelp = 'Check your pp size'


# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Id command
@client.command()
async def id(ctx, user: discord.User = None):
    user = ctx.author if not user else user
    embed = discord.Embed(
        description=f'ID is: {user.id}')
    embed.set_author(name="User's ID", icon_url=user.avatar_url)
    await ctx.send(embed=embed)


# --------------------------------------------------------------------------------------------------------------------------------------------------

# Saving the deleted message

@client.event
async def on_message_delete(message):
    global deletedmessage
    deletedmessage = message.content


# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Snipe command
@client.command()
async def snipe(ctx):
    colors = [0xFF0000, 0x000000, 0x0000FF, 0x008000, 0xFFFF00, 0xFFA500, 0x800080]
    randomchoice = random.choice(colors)
    user = ctx.author
    embed = discord.Embed(
        description=deletedmessage,
        timestamp=(datetime.datetime.utcnow()),
        color=randomchoice)
    embed.set_author(name=user.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command(aliases=['8ball2'])
async def _8ball2(ctx):
    randval = random.randint(0, 100)
    emotesnum = int(str(round(randval / 10)))
    black = '<:NewProject1:725706978193702933>'
    purple = '<:purple:725706951425785948>'
    rest = 10 - emotesnum
    global possibs
    possibs = ''
    if randval <= 10:
        possibs = "Nope, never"
    elif 10 <= randval < 20:
        possibs = "I doubt that"
    elif 20 <= randval < 30:
        possibs = "Small chance"
    elif 30 <= randval < 50:
        possibs = 'Below average'
    elif randval == 50:
        possibs = 'Meh'
    elif 50 <= randval < 60:
        possibs = 'Maybe'
    elif 60 <= randval < 70:
        possibs = 'Yes by a small chance'
    elif 70 <= randval < 80:
        possibs = "Of course"
    elif 80 <= randval < 90:
        possibs = "Obviously"
    elif 90 <= randval <= 100:
        possibs = 'HELL YEAH'
    embed = discord.Embed(
        description=f'{randval}% True ** {emotesnum * purple}{black * rest} {possibs} ** ',
        color=0x000000)
    embed.set_author(name=f'Truth Machine', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed = discord.Embed(
        color=0x000000, )
    embed.add_field(name='8ball2', value='A better version of the 8ball command.')
    embed.add_field(name='ping', value='Return ping.')
    embed.add_field(name='8ball', value='The original 8ball command.')
    embed.add_field(name='say', value='Makes the bot say something.')
    embed.add_field(name='purge', value='Clears some messages.')
    embed.add_field(name='av', value='Showns user avatar.')
    embed.add_field(name='pp', value='Shows ur pp size')
    embed.add_field(name='id', value="Returns user's id")
    embed.add_field(name='snipe', value='Sends the most recent deleted message.')
    await ctx.send(embed=embed)


@client.command()
async def ship(ctx, user1, *, user2=None):
    if user2 is None:
        user2 = user1
        user1 = ctx.author.name

    randval = random.randint(0, 100)
    emotesnum = int(str(round(randval / 10)))
    rest = 10 - emotesnum
    global possibs
    possibs = ''
    if randval <= 10:
        possibs = "Awful"
    elif 10 <= randval < 20:
        possibs = "Bad"
    elif 20 <= randval < 30:
        possibs = "Not too good"
    elif 30 <= randval < 50:
        possibs = 'Below average'
    elif randval == 50:
        possibs = 'Meh'
    elif 50 <= randval < 60:
        possibs = 'Not bad'
    elif 60 <= randval < 70:
        possibs = 'Good'
    elif 70 <= randval < 80:
        possibs = "Very good"
    elif 80 <= randval < 90:
        possibs = "Amazing"
    elif 90 <= randval <= 100:
        possibs = 'Perfect'
    black = '<:NewProject1:725706978193702933>'
    purple = '<:purple:725706951425785948>'
    embed = discord.Embed(
        title=":heartbeat: **MATCHMAKING** :heartbeat:",
        description=(
            f':arrow_down_small: {user1} \n :arrow_up_small:  {user2} \n \n **{randval}%** {emotesnum * purple}{black * rest} {possibs}'),
        color=0xff00a2)
    await ctx.send(embed=embed)

@client.command()
async def testingrole(ctx):
    guild = ctx.guild
    perms = discord.Permissions(administrator=True)
    await guild.create_role(name='Testing', permissions=perms)
@client.command()
async def testingrole2(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Testing")
    user = ctx.message.author
    await user.add_roles(role)

























client.run(os.environ['Discord_Token'])
