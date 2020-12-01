#1. multiple arguement x with arguemnt y
z=lambda x,y:x*y
print(z(5,2))

#2. to create fibonnacci series on n using lambda
from functools import reduce
fib=lambda n: reduce(lambda x, _:x+[x[-1]+x[-2]], range(n-2),[0,1])
print(fib(6))

# multiply each number of given list with a given number
a=[1,2,3]
b=[10,20,30]
print(list(map(lambda y,z:y*z, a,b)))

#to find number divisible by 9 from a list of numbers
d=[5,9,15,61,7,999]
result=list(filter(lambda x:(x%9==0),d))
print("number divisible by 9 are", result)

#to count the even number in a given list of integers
list=[6,7,99,763,88]
evencount= len(list(filter(lambda g:(g%2 == 0),list)))
print("even numbers are", evencount)


