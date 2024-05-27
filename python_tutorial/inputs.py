prompt=input("Enter your Name: ")
message=''
message2=''
while message or message2!="quit":
    print(f"Hello,{prompt.title()} Welcome to Python Bootcamp")
    message=input("How much coding do you know (low/mid/high) : ")
    if message == "mid":
        print("You can join the bootcamp")
    if message=="high":
        print("Welcome to the camp")
    if message =="low":
        print(f"Sorry, {prompt.title()} read some documentation")
    message2=input("interactive learning or Video course ?")
    if message2=='interactive':
        print(f"Good choice visit : https://github.com/Akhil-Tesla")
    if message2=='video':
        print(f"Feel free to visit youtube.com/freecodecamp ")
    break

print("Thank You")
