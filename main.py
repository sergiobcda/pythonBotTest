import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('BotTest is logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user :  
        print('channel = ', message.channel.name)
        return
    if message.content.startswith('$test') and message.channel.name == 'programacion-anal':
        await message.channel.send('botTest: command received')

client.run(os.getenv('TOKEN'))
