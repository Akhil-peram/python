"""# loop through a string 
strings='google is trillion company'
for s in strings:
    print(s)
"""
# looping numbers with range
for i in range(10):
    print(i,end=',')

squares=[i*i for i in range(5)]
evens=[i for i in range(10) if i % 2]
primes=[i for i in range(20) ]
print("\n",primes)
print("\n",evens)
print("\n",squares)
