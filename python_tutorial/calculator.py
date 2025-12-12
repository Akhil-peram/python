# calculator in OOP
class Calculator:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def add(self):
        return f"{self.x} + {self.y} = {self.x + self.y}"

    def sub(self):
        return f"{self.x} - {self.y} = {self.x - self.y}"

    def div(self):
        return f"{self.x} / {self.y} = {self.x / self.y}"

    def multiple(self):
        return f"{self.x} * {self.y} = {self.x * self.y}"


cal = Calculator(9, 5)

print(cal.add())
print(cal.multiple())

