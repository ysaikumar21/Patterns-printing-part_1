def Star_Spaces(n):
    print(' '*(n+1),'*')
    for i in range(1,n-1):
        print(' '*(n-i),'*',end='')
        print(' '*(2*i),'*')
    print(' '*1,'*'*(n+(n+1)))
n=5
result=Star_Spaces(n)
print(result)