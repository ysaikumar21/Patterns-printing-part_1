def Number_bottom_left_rightangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()
n=int(input("enter no of rows : "))
result=Number_bottom_left_rightangle(n)
print(result)