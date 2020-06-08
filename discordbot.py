import discord

TOKEN = 'TOKEN'

client = discord.client()

@client.event()
async def on_ready():
    print('ログインしたよ')

@client.event()
async def on_message(message):
