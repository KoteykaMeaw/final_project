import discord
import os
import random
from discord.ext import commands
from discord import app_commands
bot = commands.Bot(command_prefix='/',intents= discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is Up and Ready!")
    try:
        synched = await bot.tree.sync()
        print(f'Synched {len(synched)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name='hello',description='Hello for you!')
async def hello(interaction: discord.Integration):
    await interaction.response.send_message(f'Hello {interaction.user.mention}!')


@bot.tree.command(name='help',description='All bots commands')
async def hello(interaction: discord.Integration):
    await interaction.response.send_message(f'Commands are : help, global_warming, global_warming2, hello.')



@bot.tree.command(name='global_warming',description='Random global warming meme!')
async def global_warming(interaction: discord.Integration):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await interaction.response.send_message(file=picture)
    
@bot.tree.command(name='global_warming2',description='Random global warming meme but another pictures!')
async def global_warming2(interaction: discord.Integration):
    images2 = os.listdir('images2')
    img_name2 = random.choice(images2)
    with open(f'images2/{img_name2}', 'rb') as f:
            picture2 = discord.File(f)
    await interaction.response.send_message(file=picture2)
    
bot.run('token')
