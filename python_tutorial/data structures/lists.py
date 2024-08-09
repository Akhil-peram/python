# Let's create a list ; List can be made using square brackets [] any object with a square bracket is a List

companies=['Google','Apple','Amazon','Facebook','Netflix',9000,369,1,11,9.0,]

print(companies)
print(companies[0])
print(companies[3])
print(companies[0][1])
print(companies[3][2])
print(companies[1].upper())
print(len(companies))
print(companies.count('Apple'))
companies.append('Nvidia')
print(companies)
companies.extend(["madara",'itachi','susano'])
print(companies)
print(companies[3:])
print(companies[:4])
print(companies[0:5])
print(companies[:-1])
#reversing a List is easy can be done in two ways 
# method 1 by slicicng wih negative
print(companies[::-1])

#method2 by using reverse() method
companies.reverse()
print(companies)
# placing an object at specified index
companies.insert(1,'IBM')

# deleting an object in list by del or remove 
del companies[3]
print(companies)

companies.remove(9000)
print(companies)
companies.remove("Facebook")
print(companies)

# removing by pop method 
#you can pop an item using it's index too
companies.pop()
print(companies)

# copying a list by using [:]
my_list=companies[:]
print(my_list)
print(companies)
