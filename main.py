import os
import discord
from maxembeds import EmbedBuilder
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("ODkyNjU3NzY3NzU0NjU3Nzky.YVQGVA.-85gtANn0A06zrAxSxZHFJY-SpU")

client = discord.Client()


@client.event
async def on_ready():
  # Print this when the bot starts up for the first time.
  print(f"{client.user} has connected to Discord!")

@client.event
async def on_message():
  # Ignore messages from the bot itself so that there's no conflict.
  if message.author == client.user:
    return

  if message.author == 'thanks':
    # Respond to thanks.
    await message.channel.send("You're welcome!")

@client.event
async def on_message(message):
  if not message.author.bot:
    if message.content.starswith("MaxEmbeds"):
      embed = EmbedBuilder (
        title = "PyEmbedder",
        description = "This bot can post embeds with codeblocks. It's made using Python 3.9.7",
        color = discord.Color.red(),
        fields = [["Field 1", "Test field", True], ["Field 2", "Test field", True]],
        footer = ["Test footer", message.author.avatar_url],
        author = [message.author.name, message.author.avatar_url],
        thumbnail = message.author.avatar_url
      ).build()
      
      await message.channel.send(embed=embed)


client.run(token)