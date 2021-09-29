# Import libraries.
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime

# Setup main.env and run Discord.
load_dotenv()
token = os.getenv('token')
client = discord.Client()
bot = commands.Bot(command_prefix='>!')

# Events for the bot to perform.
@client.event
async def on_ready():
  # Print this when the bot starts up for the first time.
  print(f"{client.user} has connected to Discord!")

@client.event
async def on_message(message):
  # Ignore messages from the bot itself so that there's no conflict.
  if message.author == client.user:
    return

  if message.content == 'thanks':
    # Respond to thanks.
    await message.channel.send("You're welcome!")

# Bot commands.
@bot.command()
async def ping(ctx):
  await ctx.send('pong')

@bot.command()
async def info(ctx):
  embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
  embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
  embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
  embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
  embed.add_field(name="Server ID", value=f"{ctx.guild.id}")

  await ctx.send(embed=embed)

@bot.listen()
async def on_message(message):
  if "ytc" in message.content.lower():
      await message.channel.send('https://www.youtube.com/Schitzor')
      await bot.process_commands(message)


client.run(token)
