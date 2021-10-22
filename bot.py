import os
import random

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = int(os.getenv('DISCORD_GUILD'))

bot = commands.Bot(command_prefix='.')

client = discord.Client()

# @client.event
# async def on_ready():
#     guild = discord.utils.get(client.guilds, id=GUILD)

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')

print("bot active")

@bot.command(name='bonkziq')
async def nine_nine(ctx):
    ziq_bonks = [
        'ziq bonk bonk bonk',
        'i bonked the ziq',
        'consider ziq bonked',
        'bonked ziq'
    ]

    response = random.choice(ziq_bonks)
    await ctx.send(response, file=discord.File('image0.gif'))

bot.run(TOKEN)