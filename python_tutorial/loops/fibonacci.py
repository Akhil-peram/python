n=int(input("Enter the last number for Fibonacci series : "))
a,b=0,1
while a<n:
    print(a,end=",")
    a,b=b,a+b
    
