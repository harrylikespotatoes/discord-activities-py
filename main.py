import platform
import os
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot, BucketType, cooldown, CommandOnCooldown
import discordTogether
from datetime import *

command_prefix=commands.when_mentioned_or(['da!', 'fiejwhuisdbyhuoi prefix here', 'this is a list lewbsfydhiuxojnkb guhyiuh43owjenfksd'])
#you can put your own prefix here. if you want multiple prefixes, edit the list

TOKEN = 'token here'
#your bot token here
#go to https://discord.com/developers and click on your application

togetherControl = discordTogether.DiscordTogether(client)
now = datetime.now()

client = commands.Bot(command_prefix)
client.remove_command('help')

@client.event
async def on_ready():
  print(f"Logged in as {client.user.name}")
  print(f"Discord.py API version: {discord.__version__}")
  print(f"Python version: {platform.python_version()}")
  print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
  print("Bot started at: " + (now.strftime('%H:%M:%S on %a, % the %dth, %Y')))
  print("---------------------")
  global startdate
  startdate = datetime.now()

@client.command()
async def uptime(ctx):
    now = datetime.now()
    uptime = startdate - now
    await ctx.send(f'Uptime: {uptime}')

#command error handlers
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    embed = discord.Embed(
      title="Error!",
      description="Command not found \n run `da!help` to see all the commands",
      colour = 0xE02B2B
    )
    await ctx.send(embed=embed)
  elif isinstance(error, CommandOnCooldown):
    embed = discord.Embed(
      title='Calm down!',
      description='That command is on cooldown. Try again later.',
      colour = 0xE02B2B
    )
    await ctx.send(embed=embed)

#########################################################################

#cogs and perms
owner_id='727484628486848552'

#guild id stuff
@client.command(aliases=['guilds', 'guild', 'servers', 'server'])
async def guildids(ctx):
  if ctx.message.author.id == (owner_id):
    for guild in client.guilds:
      await ctx.send(f"{guild.id} : {guild.name} : + f"<@{guild.owner.id}>")
  else:
    embed = discord.Embed(
      title="Error!",
      description="Command not found \n run `da!help` to see all the commands",
      colour = 0xE02B2B
    )
    await ctx.send(embed=embed)

#########################################################################

@client.command(aliases=['l'])
async def load(ctx, extension):
  if ctx.message.author.id == int(owner_id):
    client.load_extension(f'cogs.{extension}')
    print('loaded specified cog')
    await ctx.send('Loaded specified cog.')
  else:
    await ctx.send("You don't have the permissions required to run this command.")

@client.command(aliases=['u'])
async def unload(ctx, extension):
  if ctx.message.author.id == int(owner_id):
    client.unload_extension(f'cogs.{extension}')
    print('unloaded specified cog')
    await ctx.send('Unloaded specified cog.')
  else:
    await ctx.send("You don't have the permissions required to run this command.")

@client.command(aliases=['r'])
async def reload(ctx, extension):
    if ctx.message.author.id == int(owner_id):
      client.unload_extension(f'cogs.{extension}')
      client.load_extension(f'cogs.{extension}')
      print('reloaded specified cog')
      await ctx.send('Reloaded specified cog.')
    else:
      await ctx.send("You don't have the required permissions to run this command.")

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f"cogs.{filename[:-3]}")


##################################################################

#status task
@commands.is_owner()
@client.command(aliases=['sst'])
async def startstatustask(ctx):
  if ctx.message.author.id == int('727484628486848552'):
    print('status task manually started')
    await ctx.send('Status task manually started')
    for i in range(69420):
      statuses = ['Fishington.io', 'Poker', 'Chess in The Park', 'Youtube', 'Betrayal.io']
      await client.change_presence(activity=discord.Game(random.choice(statuses)))
      time.sleep(300)
      print(f'status updated ({x+1})')

#####################################################################

#discord activities
#youtube
@client.command(aliases=['yt', 'youtub', 'youtube.com'])
@cooldown(1, 5, BucketType.user)
async def youtube(ctx):
    if ctx.author.voice == None:
        embed = discord.Embed(
            title="ERROR!",
            description="You need to connect to a vc before you can start youtube",
            colour=0xE02B2B
        )
        await ctx.send(embed=embed)
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube', max_age=60)
    embed = discord.Embed(
        title="Here's your link",
        description=(f"click the link to start youtube \n{link} \n{link}\n{ctx.message.author.mention}"),
        colour=ctx.author.colour
    )
    await ctx.send(embed=embed)

#chess
@client.command()
@cooldown(1, 5, BucketType.user)
async def chess(ctx):
    if ctx.author.voice == None:
        embed = discord.Embed(
            title="ERROR!",
            description="You need to connect to a vc before you can start chess",
            colour=0xE02B2B
        )
        await ctx.send(embed=embed)
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'chess', max_age=60)
    embed = discord.Embed(
        title="Here's your link",
        description=(f"click the link to start chess \n{link}\n{ctx.message.author.mention}"),
        colour=ctx.author.colour
    )
    await ctx.send(embed=embed)

#fishington
@client.command(aliases=['fish', 'fishing', 'fishington.io'])
@cooldown(1, 5, BucketType.user)
async def fishington(ctx):
    if ctx.author.voice == None:
        embed = discord.Embed(
            title="ERROR!",
            description="You need to connect to a vc before you can play fishington.io",
            colour=0xE02B2B
        )
        await ctx.send(embed=embed)
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'fishing', max_age=60)
    embed = discord.Embed(
        title="Here's your link",
        description=(f"click the link to start fishington.io \n{link}\n{ctx.message.author.mention}"),
        colour=ctx.author.colour
    )
    await ctx.send(embed=embed)

#poker
@client.command('poke')
@cooldown(1, 5, BucketType.user)
async def poker(ctx):
    if ctx.author.voice == None:
        embed = discord.Embed(
            title="ERROR!",
            description="You need to connect to a vc before you can play poker",
            colour=0xE02B2B
        )
        await ctx.send(embed=embed)
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'poker', max_age=60)
    embed = discord.Embed(
        title="Here's your link",
        description=(f"click the link to start poker \n{link}\n{ctx.message.author.mention}"),
        colour=ctx.author.colour
    )
    await ctx.send(embed=embed)

#betrayal.io
@client.command(aliases=['betrayal.io', 'amongus', 'amogus', 'susus_amogus', 'whats_so_funny_about_susus_amogus', "what's_so_funny_about_susus_amogus"])
@cooldown(1, 5, BucketType.user)
async def betrayal(ctx):
    if ctx.author.voice == None:
        embed = discord.Embed(
            title="ERROR!",
            description="You need to connect to a vc before you can play betrayal.io",
            colour=0xE02B2B
        )
        await ctx.send(embed=embed)
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal', max_age=60)

    embed = discord.Embed(
        title="Here's your link",
        description=(f"click the link to start betrayal.io \n{link}\n{ctx.message.author.mention}"),
        colour=ctx.author.colour
    )
    await ctx.send(embed=embed)

###########################################################################

client.run(TOKEN)
#imagine
