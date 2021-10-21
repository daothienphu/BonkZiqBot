import os
import random

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('DISCORD_GUILD'))

bot = commands.Bot(command_prefix='.')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, id=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@bot.command(name='bonkziq')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'ziq bonk bonk bonk',
        'i bonked the ziq',
        'consider ziq bonked',
        'bonked ziq'
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response, file=discord.File('bonkziq.png'))

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     brooklyn_99_quotes = [
#         'ziq bonk bonk bonk',
#         'i bonked the ziq',
#         'consider ziq bonked',
#         f'{message.author.name} bonked ziq'
#     ]

#     if message.content == '.bonkziq':
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)
#     elif message.content == 'raise-exception':
#         raise discord.DiscordException

# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise

bot.run(TOKEN)