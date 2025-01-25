name=' Akhil Peram uzumaki '
company="Google"
print(name.title())
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name,end='....')
print(name,sep=',')
print(name.count('a'))
print(name.rstrip())
print(name.lstrip())
print(name.split('.'))
print(f"Hello , {name} and welcome to {company}")
print("Hello,{} and welcome to {}".format(name,company))
print("Hello %d ",name)

# to print a quote inside a string always use backslash or single quotes to print output

message = 'Hello , " i am electron" '
print(message)

message2 = "I am from \"Space\" Andromeda galaxy"  # \ "string\" to print the quote
print(message2)
