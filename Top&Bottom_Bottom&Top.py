def Top_Bottom_Bottom_Top(n):
    for i in range(1,n+1):
        for k in range(1,i):
            print(" ",end='')
        for j in range(1,n+2-i):
            print('*',end=' ')
        print()
    for i in range(1,n+1):
        for j in range(1,n+1-i):
            print(' ',end='')
        for k in range(1,i+1):
            print('*',end=' ')
        print()
n=int(input('enter no of rows : '))
result=Top_Bottom_Bottom_Top(n)
print(result)