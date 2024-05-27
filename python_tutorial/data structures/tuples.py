# tuples are immutable 
tup=('amazon',90,'jack','captain',90,['super','spider'],'jack the slayer','sumo')
print(tup[0])
print(tup[1:])
print(tup[:3])
print(tup[::-1])
print(tup.index('captain'))
print(tup.count('jack'))

# looping through tuples
for i in tup:
    print(i)

    
