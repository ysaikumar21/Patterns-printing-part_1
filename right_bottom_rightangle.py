def Space_Star(n):
    for i in range(0,n):
        for k in range(0,n-1-i):
            print(" ",end=" ")
        for j in range(0,i+1):
            print("*",end=" ")
        print()
n=int(input("enter a number : "))
result=Space_Star(n)
print(result)