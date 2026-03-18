class Sports:
    def __init__(self, name, players, ground):
        self.name = name
        self.players = players
        self.ground = ground

    def is_sport(self):
        return True if self.ground == "yes" else False
