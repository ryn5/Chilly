import os
import discord
from discord import app_commands

import responses
from dotenv import load_dotenv
from discord.ext import commands
from chilly.cmds import *


async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    load_dotenv('.env')  # Ask for .env file and paste into root
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = commands.Bot(command_prefix='<', intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        await client.tree.sync()
        print(f'Command tree synced')

    @client.event
    async def on_message(message):
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Prevent spam
        if message.author == client.user or channel != 'dev':
            return

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel}) '{message}")

        await send_message(message, user_message)

    # Slash commands
    # For details on ctx, go to:
    # https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=context#discord.ext.commands.Context
    @client.tree.command(name="roll", description="Roll a 6-sided die")
    async def roll_cmd(ctx):
        await roll.execute(ctx, 6)

    @client.tree.command(name="rolln", description="Roll a die with the given upper bound")
    @app_commands.describe(number="Pick an upper bound")  # Parameters separated by commas
    async def roll_n_cmd(ctx, number: int):
        await roll.execute(ctx, number)

    client.run(TOKEN)
