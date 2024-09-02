def left_top_right_angle(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print('*',end=' ')
        print()
n=int(input("enter a number of rows : "))
result=left_top_right_angle(n)
print(result)
