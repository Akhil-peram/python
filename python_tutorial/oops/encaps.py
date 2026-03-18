class Marvel:
    def __init__(self, character, power, movies):
        self.character = character
        self.movies = movies
        self.__power = power

    def get_power(
        self,
    ):  # We need a get method to access the attribute since power is private
        return self.__power

    def secret_power(self):
        return f" Power is a secret and it is {self.get_power()}"


spiderman = Marvel("superhero", "spider power", 5)

print(spiderman.get_power())

# if we print power we will get an error
# print(spiderman.power)

# but we can access other attributes since they are public
print(spiderman.character)
print(spiderman.movies)
