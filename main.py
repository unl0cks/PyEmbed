# Import libraries.
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Setup main.env and run Discord.
load_dotenv()
token = os.getenv('token')
client = discord.Client()
bot = commands.Bot(command_prefix='!e')
bot = discord.Client()

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
async def displayembed(ctx):
  embed = discord.Embed(title="Your title here", description="Your desc here") #,color=Hex code
  embed.add_field(name="Name", value="you can make as much as fields you like to")
  embed.set_footer(name="footer") #if you like to
  await ctx.send(embed=embed)


client.run(token)
