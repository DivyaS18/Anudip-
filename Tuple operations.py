#Tuple Operations
# Empty tuple
t1 = ()
print("Empty Tuple:",t1)

# Tuple with one element (note the comma)
t2 = (1)
print("\nTuple with 1 element:",t2)

# Tuple with multiple elements
t3 = (1, 2, 3, 4, 5, 6, 2, 4)
print("\nTuple with multiple element:",t3)

# Nested tuples
t4 = (1, (2, 3), (4, 5, 6))
print("\nNested tuple:",t4)

# Accessing elements using indexing
print("\nAccessing element at index 0 of multiple elements tuple:",t3[0])

# Accessing elements using negative indexing
print("\nElement at last index of multiple elements tuple:",t3[-1])

# Slicing tuples
print("\nTuple from position 2 to 5 of multiple elements tuple:",t3[1:5])

# count() function
print("\nCount of 2 of multiple elements tuple:",t3.count(2)) 

# index()
print("\nFinding index of number 3 of multiple elements tuple:",t3.index(3))

#concatenation
t5 = (1, 2, 3)
t6 = (4, 5, 6)
t7 = t5 + t6
print("\nTuple 1:",t5)
print("\nTuple 2:",t6)
print("\nAdding 2 tuples:",t7)

#repetition
print("\nTuple repeated",t5 * 2)

#iteration
print("\nIteration of tuple:")
for item in t5:
    print(item)
    
#len() function
print("\nLength of tuple:",len(t5))

#max() function
print("\nMaximum digit in the tuple:",max(t5))

#min() function
print("\nMinimum digit in the tuple:",min(t5))  

#sum() function
print("\nSum of digits in the tuple:",sum(t5))

#sorted() function
t8=(5,9,1,67,34,6)
print("\nSorting the tuple:",sorted(t8))

#tuple() function for Converting an iterable (like a list) into a tuple
lst = [1, 2, 3]
print("\nConverting list into tuple:",tuple(lst)) 

#nested tuple
t9 = (1, (2, 3), (4, 5, 6))
nested_element = t9[1][0] 

# print the tuple in backward direction using forward indexing
tuple=(1,2,3,4,5)
print("\nTuple is:",tuple)
print("\nDisplay the element of tuple in backward direction using forward indexing: ")
x=len(tuple)-1
for i in range(x,-1,-1):
  print(tuple[i],end=',')

#print the tuple in forward direction using backward indexing
tuple=(1,2,3,4,5)
print("\nTuple is:",tuple)
print("\nDisplay the element of tuple in forward direction using backward indexing: ")
x=len(tuple)
for i in range(-x,0):
  print(tuple[i],end=',')
  
