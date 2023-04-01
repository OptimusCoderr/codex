#NUMPY
import numpy as np

"""""
a=np.array([1,2,3,5,7])
b=np.array((2,3,4,5))#all elements of np.array must have the sme data types
print(type(a))
print(type(b))
print(a.dtype)
a=np.array([1,2,3,5,7],dtype='int')
b=np.array((2,3,4,5),dtype='f')
print(a.dtype)
print(b.dtype)
"""""

#NUMPY DIMESNIONS
"""""
a=np.array([[2,3,4],[6,7,9]])
print(a.ndim)
b=np.array([[[1,23,4],[4,5,6]],[[5,8,9],[8,0,12]]])
print(b.ndim)
print(a[0,2])
print(b[1,1,2])
"""

#SHAPE
a=np.array([[2,3,4],[6,7,9]])
b=np.array([[[1,23,4],[4,5,6]],[[5,8,9],[8,0,12]]])
print(a.shape)
print(b.shape)
print(b.size)#TOTAL NO OF ELEMENTS IN AN ARRAY
print(b.nbytes)

#NUMPY (ARANGE,RANDOM,RESHAPE)
c=np.arange(100)
print(c,"\n")
k=np.arange(20,100)
i=np.arange(20,100,2)
print(k,"\n")
print(i)

o=np.random.permutation(np.arange(10))
print(o)
l=np.random.randint(1,30,2)
print(type(l))

"""""
u=np.random.rand(1000)
import matplotlib.pyplot as plt
plt.hist(u,bins=100)
plt.show()

B=np.random.randn(100000)
plt.hist(B,bins=200)
plt.show()
"""""
C=np.random.randn(2,3)
print(C)
print(C.ndim)

C=np.random.randn(2,3,4,2)
print(C)
print(C.ndim)

D=np.arange(100).reshape(4,25)
D.shape
print(D)

#INDEXING OR SLICING IN NUMPY [start:end:step]
A=np.arange(100)
b=A[3:9]
print(b)
b[0]=-1200
print(A)

b=A[3:9].copy()
print(b)
print(A[::5])
print(A[::-5])
print(A[::-1])

idx=np.argwhere(A==-1200)[0][0]
print(idx)
A[idx]=3
B=(A==-1200)*np.arange(A.size)
print(B)

A=np.round(10*np.random.rand(5,4))
print(A)
A[1,2]
c=A[1,:]# calling the 2nd row
g=A[:,1]# calling the 2nd column
A[1:3,2:4]#submatrix
print(c)

import numpy.linalg as la
t=la.inv(np.random.rand(3,3))
print(t)
A=np.round(10*np.random.rand(5,4))
w=A.sort(axis=0)#SORT ROWS
ww=A.sort(axis=1)#SORT COLUMN
print(w)
print(ww)

#MORE ON INDEXING

#A[index_array]
A=np.arange(100)
B=A[[3,5,6]]

B[0]=-4
print(B)
print(A)
B=A[A<40]
print(B)
B=A[(A<40) & (A>30)]
# / is used for arrays 'or' is used for single objects
# ~ is used for arrays 'not' is used for single objects
# & is used for arrays 'and' is used for single objects
print(B)


# BOARDCASTING
E=np.round(np.random.rand(2,3))
print(E)
E=E+[5,1,8]
print(E)

#hstack, vstack, sort(axis=0)
B=np.round(10*np.random.rand(2,2))
C= np.hstack((E,B))
print(C)
G=np.random.permutation(np.arange(10))
print(G)
G=np.sort(G)
print(G)
G.sort()
G=G[::-1]
print(G)

#NUMPY (SPEED:UFUNCS)
b=np.random.rand(10000000)
help(time)
%timeit sum(b)
%timeit np.sum(b)
%%timeit
s=0
for x in b:
    s+=x



