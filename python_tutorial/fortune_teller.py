import random

def guess_fortune(fortune):
    if fortune == 1:
        return "You have good Fortune"
    elif fortune == 2:
        return "Believe in yourself"
    elif fortune == 3:
        return "Life is a race run , run"
    elif fortune == 4:
        return "Its time to remember who you are"
    elif fortune == 5:
        return "world is fake"
    else:
        return "Luck doesn't matter to you , work"
    
fortune=random.randint(1,6)
print(guess_fortune(fortune))
    