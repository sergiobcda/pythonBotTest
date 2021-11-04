import Command
'''
Clase HelloUserCommand
Se trata de un comando concreto que solo devuelve el saludo a un usuario
'''
class HelloUserCommand(Command):
    pass

'''def __init__(self):
    self = Command()'''

async def exec(self, message):
    stringMessage = message.content.split()
    error = self.name in stringMessage[1]
    if not error:
        await message.channel.send('Hello user ', message.user.name)
    return not error