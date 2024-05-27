"""
def greet():
    print("hello")

greet()
"""
# function 2 

def greeter(name, age, place):
    print(f"Hello {name} Welcome")
    if age>18 and age<90:
        print(f"you can vote {name}")
    elif age <18:
        print(f"Drink milk")
    else:
        print("You are too small")

    print(f"Nice place, {place}")

greeter("jack",1,"nyc")