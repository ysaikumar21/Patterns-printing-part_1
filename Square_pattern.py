def Square_pattern(n):
    for i in range(n):
        for j in range(n):
            print('*',end=" ")
        print()
n=int(input('Enter a positive number : '))
result=Square_pattern(n)
print(result)