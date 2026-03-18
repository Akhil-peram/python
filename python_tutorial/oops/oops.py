class Character:
    def __init__(self, name, anime, power):
        self.name = name
        self.anime = anime
        self.power = power

    def hero(self):
        return f"Hero is {self.name}"

    def anime_name(self):
        return f"Anime is {self.anime}"


char = Character("Naruto uzumaki", "Naruto", "Ninjitsu")


print(char.hero())
print(char.anime_name())
