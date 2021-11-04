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
        result = self.syntax in stringMessage[1]
        if result:
            response = 'Hello user ' + message.author.name
            await message.channel.send(response)
        return result