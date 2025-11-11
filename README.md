# Python Tutorial
----------------------------------------------------------------------------------------------------------------------------------------------
**Basic python programming code** 
### Variables 
### Strings
### Conditional statements
### Oops 
### File handling and Exceptions
### Modules 
### Data structures
## My Section Title

You can [jump to My Section](#my-section-title) from here.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- The classic hello world program

          print("Hello World")

          print(f"Hello world") # f-strings

          print('Hello World')
     
          print("Hello ,I am Ironman")
 
 
## variables [variables](#variables) from here


variables store data ,

literally literals String , integer , float etc....

      name = "John wick"
      age = 39
      occupation = "Assassin"
      height = 6.1
      net = 50_00_000
      print(name,age, occupation , height , net)
## Operators
- Arithmetic operators
  The Mathetical operations in python using Arithmetic operators.Python can be used as a calculator

       apples = 11
       mangoes = 9

       print(apples + mangoes)

       print(apples - mangoes)

       print(apples / mangoes)
- Membership operators

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
  
- Relational operators
   The comparison operators that gives a boolean 'True' and 'False'

  
       """ > greater than
           < lesss than
           != not equal 
           >= greater than or equal to
           <= less than or equal to
       """
        a = 3
        b = 6
        c = 9
        print(a>b)
        print(a<b)
        print(b<c)
        print(c>=a)
         
       
- Logical operators
   The logical operators are and , or


 ## Strings

 
  A sequence data type which stores a character (i.e A group of characters is called a string or just one character sometimes :)
  In python anything in between quotes either " " or ' ' is a string

       name="Ironman"
       space="" # just one space character
       nums="123456789"
       symbols="!@#$%^&*()"
       pc='tron'

       # strings can be concatenated using " + " 

       
       print(name + space + nums + symbols + pc)
       print(name +" "+ space+" "+ nums +" "+ symbols +" "+ pc)
       print("Hello"+","+"Everyone")
- Let's talk more abou strings , strings are the godly power and string methods are weapons
- Every variable is an object in python , hence they have methods like

                              name='Naruto uzumazki'
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
  `
## Conditionals
if statements
Loops

* if statements
* elif
* else

### if statement

          age =19
          if age > 18:
              print("You can drive")
          print("Bye")


### else Statement


        name = input("Enter passkey")
        # passkey = "Naruto"
        if name == "Naruto":
            print("You may pass")
        else:
             print("Not allowed")
  
### elif statement (elseif)

    name = input("Enter pass key")
    if passkey == "Naruto":
        print("You may pass")
    elif:
       print("You misplaced the key")

    else:
      print("Not allowed")



