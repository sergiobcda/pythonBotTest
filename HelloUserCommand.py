from Command import Command
'''
Clase HelloUserCommand
Se trata de un comando concreto que solo devuelve el saludo a un usuario
'''
class HelloUserCommand(Command):

    def __init__(self):
        self.name = 'Hello User Command'
        self.syntax = 'hello'
        #Command.super('Hello User Command', 'hello')

    async def exec(self, message):
        stringMessage = message.content.split()
        error = self.syntax in stringMessage[1]
        if not error:
            await message.channel.send('Hello user ', message.user.name)
        return not error