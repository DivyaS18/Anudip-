import numpy as np

l=([10,30,25,43,21])
arr=np.array(l)
print("printing array",arr)


a=np.array(42)
b=np.array([1,2,3,4,5])    #vector
c=np.array([[1,2,3],[4,5,6]])  #matrix
d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])     #tensor

print("\na array:",a)
print("b array: ",b)
print("c array: ",c)
print("d array: ",d)

print("\na array dimen ",a.ndim)
print("b array dimen ",b.ndim)
print("c array dimen ",c.ndim)
print("d array dimen ",d.ndim)
print("c array shape",c.shape)

#slicing
sarr=arr[1:5]
print("\nSimple array:",arr)
print("Sliced array",sarr)

sarr[2]=100

print("\nSimple array after inserting 100 at index 2",arr)
print("Sliced array after inserting 100 at index 2",sarr)     #if we make changes in the sliced arr the original arr will also change as by default slicing uses view

#copy
arr2=arr.copy()
arr[0]=42
print("\nSimple array",arr)
print("Copied array",arr2)

x=arr.view()              #if we change in view the original arr will also change 
arr[0]=45
print("\nSimple array",arr)
print("Array using view function",x)


#numpy zeros() without dtype and order
a=np.zeros(6)
print("\nwithout dtype and order",a)

#with order
a=np.zeros((6,),dtype=int)
print("\nwith order",a)

#with shape
a=np.zeros((6,2))
print("\nwith shape",a)

#creating 1
a=np.ones((6,2))
print("\nCreating ones:",a)

#with 5
a=np.ones((6,2))*5
print("\ncreating ones with 5:",a)

#create 1d array of ones
arr=np.ones(5, dtype=int)
print("\ncreating 1d array of ones:",arr)

#an array with 6 ones and integer data type
arr=np.ones((6,), dtype = int)
print("\nan array with 6 ones and integer data type:",arr)

#create 2d array with ones
arr=np.ones((3,4))
print("\ncreate 2d array with ones",arr)

#use 2 d array with ones
arr=(3,4)
arr2=np.ones(arr)
print("\nuse 2 d array with ones",arr2)


#creates an identity matrix
arr4=np.eye(3)
print("\nIdentity Matrix:",arr4)

#diagonally generates number
arr5=np.diag((3,4,1,6))
print("\ndiagonally generated array",arr5)
print("array shape",arr5.shape)
