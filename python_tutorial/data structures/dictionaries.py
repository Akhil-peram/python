dict={"name":"Akhil","age":22,"skill":"Machine learning, Data science, python , c , c++"}
print(dict)
print(dict["name"])
print(dict['skill'])
# To add new key: value pairs 
dict["hobby"]="coding"
dict["height"]=5.11
dict["place"]="india"
dict["arrogance"]=1000
print(dict)

# to modify a key value assign with new value 
dict["hobby"]="coding,Gaming,Martial arts","Fighting" # you can add values seperated by comma to
print(dict)

# to delete a key value pair use del statement
del dict["arrogance"]
print(dict)

# looping through the keys and values in dictionary
for key,value in dict.items():
    print(key,"-->",value)
# wecan use naming conventionas we like
for k,v in dict.items():
    print(f"keys: {k} and values are => {v}")

# looping only through keys 
for k in dict.keys():
    print("this is key, ",k)
# looping through the values 
for values in dict.values():
    print(f"These are values: {values}")
# dictionary inside a dictionary
"""
Dictionaries inside dictionaries doesnt take assignments("=")
always use colo(:) and new line indents 
"""
scientist={
    "nerd1":{
        "Name":"Nikola tesla",
        "power":"AC current",
        "from":"Us",
        "age":95
    },

    'nerd2':{
        "name":"isaac Newton",
        'power':'Gravity',
        'from':'UK',
        'Age':68}


}

for name,power in scientist.items():
    print(name,",",power)


