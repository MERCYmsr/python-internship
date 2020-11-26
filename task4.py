A=[1,2,3,4]
second_element=A[2]
print(A[1:2])
print(A[-1])

A.append(2)
print(A)

B=[5,6,7,8]
A.extend(B)
print(A)

A.insert(2,A)
print(A)

del A[2]
print(A)
second_element=A.pop()
print(A)
second_element=A.pop(0)
print(A)
A.remove(A[0])
print(second_element)
second_element=min(A)
print(A)
second_element=max(A)
print(A)

A.sort()
print(A)

my_tuple=("day",2,"day improment")
print(my_tuple)
my_tuple=(1,2,3,4,5,8)
print(my_tuple[0])

x=[10,9,8,7,6,5,4,3,2,1]
(x.append(11))
print(x)
x.remove(8)
print(x)

X=min(x)
print(X)

X=max(x)
print(X)


M=('z','y','x','m')
M=tuple(reversed(M))
print(M)

aList=list(M)
print(aList)
































