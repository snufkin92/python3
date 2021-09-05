class Player(object):

    def __init__(self, name):
        print(f'### init {name}', id(self))
        self.name = name


class President(object):
    __instance = None

    def __new__(cls, *args, **kargs):
        print(f'### new  {args[0]}', id(cls))
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, name):
        print(f'### init {name}', id(self))
        self.name = name


jordan = Player("Jordan")
lebron = Player("LeBron")

print("Singlton")
president_1st = President("George Washington")
president_2nd = President("John Adams")
