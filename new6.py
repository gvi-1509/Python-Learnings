# any() and all()


'''from array import array

a = array('i', [10, 20, 30, 40, 50])
b = array('i', [100, 20, 300, 40, 50])

result = [x == y for x, y in zip(a, b)]

print(all(result))  
'''

#where()
'''
import numpy as np
from array import array

a = array('i', [10, 200 ,30 ,400 ,50])
b = array('i', [100, 20, 300, 40, 50])

a_np=np.array(a)
b_np=np.array(b)

result = np.where(a_np > b_np, a_np, b_np)

print(result) 
'''
#nonzero

'''import numpy as np
from array import array

a = array('i', [10, 200,0 ,30 ,400 ,0])

#a_np=np.array(a)


result = np.nonzero(a)

print(result) 

'''

#aliasing
'''
import numpy as np
from array import array

a = array('i',[10, 200,0 ,30 ,400 ,0])
b = a
#result = np.nonzero(a)
print(a)
print(b) 
'''
#view()

# import numpy as np
# from array import array

# a = array('i',[10, 200,0 ,30 ,400 ,0])
# print(a.view())
# b = a.view()
# print(a)
# print(b) 
# print("a",id(a))
# print("b",id(b)) 

'''import numpy as np

a = np.array([10, 200, 0, 30, 400, 0], dtype='i')
b = a.view()
print(a)
print(b)
print("a", id(a))
print("b", id(b))

'''
#copy

'''import numpy as np

a = np.array([10, 200, 0, 30, 400, 0], dtype='i')
b = a.copy()
print(a)
print(b)
print("a", id(a))
print("b", id(b))
'''

#Getting input from user in Numpy One Dimensional Array using for Loop Python 

'''import numpy as np

n = int(input("Enter the size of the array: "))
a = np.zeros(n, dtype=int)

for i in range(n):
    x = int(input(f"Enter element {i + 1}: "))
    a[i] = x

print("The array is:", a)'''

#Getting input from user in Numpy One Dimensional Array using while Loop Python

'''import numpy as np

n = int(input("Enter the size of the array: "))
a = np.zeros(n, dtype=int)

u = len(a)
i = 0
j = 0

while i<u:
    x = int(input("enter element="))
    a[i] = x
    i+=1

while j< len(a):
    print(a[j])
    j+=1

print(a)
'''

#Two Dimensional Numpy Array
#  using array Function in Python

''''import numpy as np
a = np.array([[10,20,30,40],
            [50,60,70,80]],dtype=float)
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[0][3])
print(a[1][0])
print(a[1][1])
print(a[1][2])
print(a[1][3])
'''

#Accessing Numpy 
# Two Dimensional Array using for Loop in Python

'''import numpy as np
a = np.array([[10,20,30,40],
            [50,60,70,80]],dtype=int)

n = len(a)

for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j])
    print() '''               


#Accessing Numpy 
# Two Dimensional Array using while Loop in Python
'''
import numpy as np

a = np.array([[10,20,30,40],
            [50,60,70,80]],dtype=int)

n = len(a)
i = 0

while i < n:
    j = 0 
    while j< len(a[i]):
        print('index' , i,j,'=',a[i][j])
        j+=1
    i+=1
    print()

'''
#Numpy Two 
# Dimensional Array using ones Function in Python


'''import numpy as np

a = np.ones((3,2),dtype=int)

n = len(a)
i = 0

while i < n:
    j = 0 
    while j< len(a[i]):
        print('index' , i,j,'=',a[i][j])
        j+=1
    i+=1
    print()

'''
























