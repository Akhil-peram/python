
# set is a colllection type data structure used to store elements without any order

set = { "ironman",1,"Batman",2}

print(set)
# set acknowledges unique elements only , i.e no duplicate elements in the set

sets = { 1,2,4,5,2,6,8,2,3,1,4}
print(sets)
# to add an element into existing set add() function is used 
sets.add('Hello')

print(sets)

# to  copy the set into a new set use copy() function / method

copy_set=sets.copy()
print(copy_set)

# to pop (delete) use pop() 
sets.pop()
print(sets)
