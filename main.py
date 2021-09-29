# Import libraries.
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime

# Setup main.env and run Discord.
load_dotenv()
gettoken = os.getenv('token')

getbot1 = commands.Bot(command_prefix='!')

# Events for the bot to perform.
@getbot1.event
async def on_ready():
  # Print this when the bot starts up for the first time.
  print(f"{getbot1.user} has connected to Discord!")

@getbot1.event
async def on_message(message):
  # Ignore messages from the bot itself so that there's no conflict.
  if message.author == getbot1.user:
    return

  if message.content == 'thanks':
    # Respond to thanks.
    await message.channel.send("You're welcome!")
  
  await getbot1.process_commands(message)

# Bot commands.
@getbot1.command()
async def ping(ctx):
  await ctx.send('pong')
  
@getbot1.command()
async def youtube(ctx):
  await ctx.send('https://www.youtube.com/Schitzor')

@getbot1.command()
async def info(ctx):
  embed = discord.Embed(title=f"{ctx.guild.name}", description="Embed bot made using Python 3.9.7.", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
  embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
  embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
  embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
  embed.add_field(name="Server ID", value=f"{ctx.guild.id}")

  await ctx.send(embed=embed)


getbot.run(gettoken)
