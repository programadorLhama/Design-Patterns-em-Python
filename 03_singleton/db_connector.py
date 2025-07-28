import random

class __DbConnector:
    def __init__(self):
        self.__id = random.randint(1, 100)
        print(self.__id)

    def connectar(self):
        print('connectado ao banco de dados')

db_connector = __DbConnector()
