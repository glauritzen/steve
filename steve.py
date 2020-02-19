import discord
import os
from discord.ext import commands

TOKEN = 'Njc5MzI0MTg5MjE1NDI0NTEy.Xkvs8w.Dr_S6QXYaH5GxYpl4U5nztK_vXs'

client = commands.Bot(command_prefix = ['!'])

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Crying for help!'))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_member_join(member):
    print(f'{member} connected to da server')

@client.event
async def on_member_remove(member):
    print(f'{member} ran away:(')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    

client.run(TOKEN)
