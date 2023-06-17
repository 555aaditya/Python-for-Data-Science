# -*- coding: utf-8 -*-
"""(2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U7gPUaew8omMLTgrrkeT1rPdf2ZMNB2X

# NUMPY

(1) Importing
"""

import numpy as np

a=np.array([1,2,3,4])
print(a)

print("\n")

b=np.array([[1,3,5,7],[2,4,6,8]])
print(b)

print("\n")

c=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(c)

print("\n")

"""(2) Dimension - gives the dimension for the array matrix

"""

import numpy as np

a=np.array([1,2,3,4])
print(a)

print("\n")

b=np.array([[1,3,5,7],[2,4,6,8]])
print(b)

print("\n")

c=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(c)

print("\n")

print(a.ndim)
print("\n")
print(b.ndim)
print("\n")
print(c.ndim)

"""(3) Shape - gives the number of row and column (x,y)"""

import numpy as np

a=np.array([1,2,3,4])
print(a)

print("\n")

b=np.array([[1,3,5,7],[2,4,6,8]])
print(b)

print("\n")

c=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(c)

print("\n")

d=np.array([5])
print(d)

print("\n")

print(a.shape)
print("\n")
print(b.shape)
print("\n")
print(c.shape)
print("\n")
print(d.shape)

"""(4) Datatype - The datatype of the values stored in the array"""

import numpy as np

a=np.array([1,2,3,4])
print(a)

print("\n")

b=np.array([5,6,7,8],dtype=float)
print(b)

print("\n")

print(a.dtype)
print("\n")
print(b.dtype)
print("\n")

"""(5) Itemsize - the memory taken by the variable"""

import numpy as np

a=np.array([1,2,3,4],dtype='int32')
print(a)

print("\n")

b=np.array([5,6,7,8],dtype='float16')
print(b)

print("\n")

c=np.array([9,10,11,12],dtype='int16')
print(c)

print("\n")

d=np.array([13,14,15,16],dtype='float32')
print(c)

print("\n")

print(a.itemsize)
print("\n")
print(b.itemsize)
print("\n")
print(c.itemsize)
print("\n")
print(d.itemsize)
print("\n")

"""(6) nbyte - it gives the total size taken (a.size * a.itemsize)"""

import numpy as np

a=np.array([1,2,3,4],dtype='float16')
print(a)

print("\n")

b=np.array([5,6,7,8],dtype='float32')
print(b)

print("\n")

print(a.nbytes)
print("\n")
print(b.nbytes)
print("\n")

"""(7) accessing elements"""

import numpy as np

a=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]])
print(a)

print("\n")

#shape
print(a.shape)

#accessing specific elements [row,column]
print(a[2,1])
print(a[-1,-5])

#accessing multiple elemetns [startRow:startColumn,endRow:endColumn]
print(a[0, :])  #prints first row
print(a[-1, :]) #prints last row

print(a[: ,2])  #prints the third column
print(a[: ,-1]) #prints the last column
print("\n")

#changing values
a[0,3] = 44
print(a)
print("\n")

a[0, :] = [6,5,4,3,2,1]
print(a)

"""(8) Random values"""

import numpy as np

#random decimals
print(np.random.rand(4,2))
print("\n")
print(np.random.rand(2,2))
print("\n")

#random integers - np.random.randint(low, high=None, size=None, dtype=int)
print(np.random.randint(1,10,size=(4,4)))
print("\n")
print(np.random.randint(1,5,size=(5,5)))
print("\n")

"""(9) Repeating an array"""

import numpy as np

# numpy.repeat(a, repeats, axis=None)

a = np.array([[1,2,3,4]])
print(a)
print("\n")
b = np.repeat(a,4,axis=0)
print(b)
print("\n")
c= np.repeat(a,4,axis=1)
print(c)

"""(10) manipulating"""

import numpy as np

a=np.ones((5,5),dtype='int8')  #print a 5x5 ones matrix
print(a)
print("\n")

b=np.zeros((3,3),dtype='int8')
b[1,1]=9
print(b)
print("\n")

a[1:-1,1:-1] = b
print(a)