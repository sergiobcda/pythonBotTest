from HelloUserCommand import HelloUserCommand

class CommandList:

    list = []

    def __init__(self):
        command = HelloUserCommand()
        self.list.append(command)


