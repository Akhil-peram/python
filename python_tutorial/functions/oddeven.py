def oddeven(n):
    print(f"Enter the last number for finding odd and even")
    for i in range(n+1):
        if i%2 == 0:
            print(f" The number {i} is even ")
        else:
            print(f"The number {i} is odd")

oddeven(30)