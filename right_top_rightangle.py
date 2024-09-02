def right_top_rightangle(n):
    for i in range(0,n):
        print("  "*i,end="")
        print("* "*(n-i))
n=int(input('enter a number: '))
result=right_top_rightangle(n)
print(result)