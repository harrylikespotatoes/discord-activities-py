import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot(command_prefix=["da!"], intents=discord.Intents.default())

class other(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
      print('extension other has been loaded')

    @commands.command()
    async def ping(self, ctx):
      latency = self.client.latency
      embed = discord.Embed(
        title="Pong! 🏓",
        description=(f"The bot latency is {latency * 1000}" + " ms"),
        colour=ctx.author.colour
      )
      await ctx.send(embed=embed)

    @commands.command(aliases=['botinvite', 'invitebot', 'inv', 'support'])
    async def invite(self, ctx):
      embed = discord.Embed(
        title='Invite and Support',
        description='`Bot Invite` \n click [here](https://discord.com/api/oauth2/authorize?client_id=889015505040596992&permissions=8&scope=bot) to invite the bot',
        colour=ctx.author.colour
      )
      embed.add_field(name="`Support Server`", value="[https://discord.gg/7cSktdJSdj](https://discord.gg/7cSktdJSdj)")

      await ctx.send(embed=embed)

      #bot info
    @commands.command(aliases=['info'])
    async def about (self, ctx):
      embed = discord.Embed(
        title='Bot Info',
        description=
          """This bot was made on <t:1610370001:D> <t:1610370001:R> \n Last updated: <t:1631918709:R> \n \n The Discord Activities bot was made by tram#1848 with the help of cold#4777 and a massive thank you to Bxllistic#4444 who made this possible. \n [here](https://pypi.org/project/discord-together/) is the pypi library link if you want to look at it yourself \n \n If you want to invite this bot, click [here](https://discord.com/api/oauth2/authorize?client_id=889015505040596992&permissions=8&scope=bot\n\nThe host used for this bot is Epikhost. It provides free and fast servers for python and js. If you're interested in hosting with Epikhost, click [here](https://dsc.gg/hosts))
          """,
        colour=ctx.author.colour
      )
      await ctx.send(embed=embed)

    @commands.command(aliases=['helps', 'commands', 'hi', 'hello'])
    async def help (self, ctx):
        embed = discord.Embed(title='List of all commands',description='`da!help` - shows this message',colour=ctx.author.colour)
        embed.add_field(name="`da!help`", value="shows this message", inline=False),
        embed.add_field(name="`da!youtube`",value="allows you to use youtube on discord \n aliases: yt, youtube.com",inline = True),
        embed.add_field(name="`da!chess`",value="allows you to play chess in the park / chess on discord \n aliases: none",inline = True),
        embed.add_field(name="`da!fishington`",value="allows you to play fishington.io on discord \n aliases: fish, fishing, fishington.io",inline = True),
        embed.add_field(name="`da!poker`",value="allows you to play poker on discord \n aliases: poke",inline = True),
        embed.add_field(name="`da!betrayal`",value="allows you to play betrayal.io on discord \n aliases: betrayal.io, amongus",inline = True),
        embed.add_field(name="`da!ping`",value="allows you to play betrayal.io on discord\naliases: none",inline = True),
        embed.add_field(name="`da!about`",value="shows more information about the bot \n aliases: info",inline = True),
        embed.add_field(name="`da!invite`",value="gives you the link for the bot invite and the support server \n aliases: support, inv,  botinvite",inline = True)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(other(client))
