def Horizontal_triangle(n,m):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('*',end=' ')
        print()
    for i in range(m,0,-1):
        for j in range(i):
            print('*',end=' ')
        print()
n=int(input("enter no of rows first half : "))
m=int(input("enter no of rows Second half : "))
result=Horizontal_triangle(n,m)
print(result)