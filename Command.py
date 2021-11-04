import discord
from abc import ABC, abstractmethod

'''
Clase abstracta Command
Contiene los atributos y metodos comunes a todos los comandos (name, exec)
al ser una clase abstracta esta no puede ser instanciada (no pueden existir objetos concretos de la clase Command)
en su lugar habra que instanciar un objeto de cualquier clase concreta hija de Command
'''
class Command(ABC):

    #command = Command()
    #command.name
    #command.message

    '''
    "Builder" o constructor de la clase, es llamada por el compilador en el momento que se crea un objeto
    de la clase Command (que en este caso sera otra clase que herede de Command por ser abstracta.
    Este metodo configura e inicializa los datos del objeto concreto
    '''
    def __init__(self, name):
        self.name = name

    '''
    Metodo abstracto, es decir que debe ser completado por cada objeto que herede de Command.
    Sera esta seccion la que diferencia entre objetos hijos en cuanto a funcionalidad
    '''
    @abstractmethod
    async def exec(self, message):
        pass
