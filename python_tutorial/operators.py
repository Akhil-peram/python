# Arithmetic operator 
print(9+9)
print(18-9)
print(5*9)
print(38/9)
print(69//9)
print(9%5)

# memebership operators in, not is

nums=[1,2,3]
print("\n",3 in nums)

cake="strawberry"
print("\n","berry" in cake)
print("\n", "mango" in cake)

# i mean literally numbers are not cake (-__-)
print("\n")
print(cake is not nums)


# id() one of the most impoertant function , it shows th storage location of a variable in the memory of cpu 
# it changes location everytime you run

score=9049
print(id(score))