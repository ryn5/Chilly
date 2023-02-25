import os
import discord
import responses


async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    load_dotenv('.env')
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = commands.Bot(command_prefix='<', intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

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

    client.run(TOKEN)
