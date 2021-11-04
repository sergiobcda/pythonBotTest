import discord
import os
from Command import Command
from CommandList import CommandList

client = discord.Client()
availableCommandsList = CommandList()

@client.event
async def on_ready():
    print('BotTest is logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    '''
    si el autor del mensaje es un usuario presenta en consola el canal del mensaje'''
    if message.author == client.user :  
        print('channel = ', message.channel.name)
        return

    '''
    si el mensaje empieza con la palabra reservada y el canal es el deseado'''
    if message.content.startswith('$test') and message.channel.name == 'programacion-anal':
        listMessage = message.content.split()
        '''
        si el mensaje contiene solo la palabra reservada (a modo de test)'''
        if len(listMessage) == 1:
            '''
            confirma la recepcion del mensaje de test'''
            await message.channel.send('botTest: command received')
        else:
            cont = 0
            '''
            itera hasta encontrar el comando correcto o agotar la lista de comandos'''
            listLenght = len(availableCommandsList.list)
            '''l = (cont < listLenght)
            command = availableCommandsList.list[cont]
            r = not (await command.exec(message))'''
            while (cont < listLenght) and not (await availableCommandsList.list[cont].exec(message)):
                cont = cont + 1
            if cont == listLenght:
                await message.channel.send('botTest: command not recognized')



client.run(os.getenv('TOKEN'))
