def Triangle_top_bottom(n):
    for i in range(1,n+1):
        for k in range(1,i):
            print(" ",end='')
        for j in range(1,n+2-i):
            print('*',end=' ')
        print()
n=int(input('enter a no of rows : '))
result=Triangle_top_bottom(n)
print(result)