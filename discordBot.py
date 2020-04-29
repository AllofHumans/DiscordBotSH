import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

VERSION_NAME = "0.0.3"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print( 
        f"{bot.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )
    game = discord.Game("endless debugging")
    await bot.change_presence(status=discord.Status.dnd, activity=game)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def version(ctx):
    await ctx.send(f"Version {VERSION_NAME}")
    
# @bot.command()
# async def help(ctx):
#     embed = discord.Embed(title="Commands", color=10038562)
#     embed.add_field(name="!version", value="Lists the version the bot is on", inline=False)
#     embed.add_field(name="!info", value="Lists information about the bot", inline=False)
#     embed.add_field(name="!iamdumb", value="Gives a statement of semi-apology for idiotic mistakes.", inline=False)
#     await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    info = discord.Embed(title="TestDiscordBot", description="Shasta's little testing bot.", color=10038562)
    info.add_field(name="Current purpose:", value="Learning python, annoying people", inline=True)
    info.add_field(name="Version:", value="0.0.3", inline=True)
    await ctx.send(embed=info)

@bot.command()
async def iamdumb(ctx):
    await ctx.send("I am dumb and I did a dumb. Ignore my dumbness.")

@bot.event
async def on_typing(channel, message, time):
    await channel.send("Hurry up.")

@bot.event
async def on_message_delete(message):
    await message.channel.send(message.author.nick + " **deleted a message that said** " + message.content)

if __name__ == "__main__":
    bot.run(TOKEN)