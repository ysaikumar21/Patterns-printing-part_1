def left_bottom_rightangle(n):
    for i in range(0,n):
        for i in range(0,i+1):
            print('*',end=' ')
        print()
n=int(input("enter a number of rows : "))
result=left_bottom_rightangle(n)
print(result)
