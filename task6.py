list=[1,2,3,4,5]
for i in list:
    print(i,i+2)

n=int(input("enter the number of row:"))
for row in range(n,0,-1):
    for column in range(1,row+1):
        print(column,end="")
    print()



