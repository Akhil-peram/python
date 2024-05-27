parrot=input("Enter your name: ")
print(f"Hi,{parrot} write something to get its length or type quit ")
message=''
while message!='quit':
    message=input("Enter message here: \n")
    print('length of string is',len(message))
print("Thank you ")
