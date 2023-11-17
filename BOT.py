import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command('global_warming')
async def warm(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command('global_warming2')
async def warm(ctx):
    images = os.listdir('images2')
    img_name = random.choice(images)
    with open(f'images2/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)


bot.run('token')
