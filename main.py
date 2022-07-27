# bot.py
import os
import random

import discord
from discord.ext import commands
# import discord.ext.commands.Context
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = {"testes"}

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    """EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE."""
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"Servidor {guild.name} - ID {guild.id}")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print(f"Este bot está em {str(guild_count)} servidores.")


@bot.command()
async def punch(ctx, arg):
    """!punch someone"""

    await ctx.send(f"Punched {arg}")


@bot.command()
async def ola(ctx):
    """
    This is defining a '!hello' command

    https://stackoverflow.com/questions/63430176/discord-bot-with-python-how-to-make-it-reply-in-the-channel-we-send-the-command/63431952#63431952
    """

    message = f"Olá, {ctx.author.mention}. Tudo bem?"
    await ctx.send(message)


@bot.command()
async def eco(ctx, *, content):
    """
    Repete o que eu disse

    https://stackoverflow.com/questions/61609453/discord-bot-ctx-only-capturing-first-word
    """
    message = "".join(content)
    await ctx.send(f"Você disse: \n> _{message}_")


@bot.event
async def on_message(msg):
    if msg.content == 'mod' and msg.author != bot.user:
        await msg.channel.send('Alguém me chamou?')


bot.run(TOKEN)

# https://stackoverflow.com/questions/66722825/get-the-message-content-into-a-command-discord-py
