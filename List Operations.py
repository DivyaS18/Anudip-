#All list operations

#creating blank list
blist=[]
print("Printing blank list:",blist)

#creating a list with single element
slist=[3]
print("\nList with single element:",slist)

#creating a list using another sequence data type
tuple_elements = (1, 2, 3, 4, 5)     # Tuple containing elements
my_list = []    #Creating an empty list
for element in tuple_elements:        # Iterating over the tuple and appending each element to the list
    my_list.append(element)
print(my_list)


#displaying complete list with formatting and multiple elements
list=[20,70,69,'hello',50]
print("\nList with formatting: ",list)

#only printing list elements without formatting
print("\nList without formatting:")
print(*list)

#forward indexing
print("\nRepresenting list with forward indexing:")
for i in range(len(list)):
    print(list[i], end=" ")


#backward indexing
print("\n\nRepresenting list with backward indexing:")
for i in range(-1, -len(list)-1, -1):
    print(list[i], end=" ")

#slicing
# Slicing from the start to index 5
print("\nSlicing from the start to index 5",list[:5]) 

# Slicing from index 5 to the end
print("\nSlicing from index 5 to the end",list[5:])  

# Slicing the entire list
print("\nSlicing the entire list",list[:]) 

# Slicing with a step of 2
print("\nSlicing with a step of 2",list[::2])  

# Slicing with negative indices
print("\nSlicing with negative indices",list[-5:-2]) 

# Slicing with a negative step (reversing the list)
print("\nSlicing with a negative step",list[::-1]) 

#accessing members using for loop
print("\n\nAccessing elements using for loop:")
for x in list:
    print(x, end=" ")

#fetching 3rd element
print("\n\n3rd element :", list[2])

#fetching 4th elemt from last
print("\n4th element from last :", list[-4])

#fetching elements from 3rd position to 10th position
print("\nElements from 3rd position to 10th position:", list[2:10])

#alternate elements from 3rd position to 10th position
print("\nAlternate elements from 3rd position to 10th position:", list[2:10:2])

#create a list of 20 numbers and print them in backward direction using forward index
print("\nCreating a list of 20 numbers and printing them in backward direction using forward index:")
mylist=[12,40,28,45,89,45,67,8,934,24,897,345,786,23,57,1,2,3,4,5]
x= len(mylist)-1
for index in range(x,-1,-1):
    print(mylist[index], end=" ")

#another list creation
mylist2=[20,30,40,50]
x=int(input("\n\nEnter any number"))  #for adding to the list

#adding an element at the end of the list using append function
print("\nAdding the element at the end of the list:")
mylist2.append(x)
print(*mylist2)


second=[1,2,3,4]   #created another list

#appending another list at the end of the list
print("\nAdding the whole list at the end of the existing list:")
mylist2.append(second)
print(*mylist2)

#using extend to add multiple elements at the end of a list
third=[5,6,7,8]    #created another list
print("\nAdding multiple elements at the end of the list:")
mylist2.extend(third)
print(*mylist2)

#inserting element at specified position
print("\nInserting element at the specified position:")
mylist2.insert(5,147)
print(*mylist2)

# Manually track the index for insertion
print("\nManually tracking the index for insertion:")
elements_to_insert = [5, 6, 7]
start_index = 2    # Starting index for insertion
index_offset = 0   # Manual index tracking variable
for element in elements_to_insert:
    current_index = start_index + index_offset          # Calculate the current insertion index
    mylist.insert(current_index, element)     # Insert the element at the current index
    index_offset += 1
    print(*mylist)
    
#printing the list before deletion
print("\nPrinting the old list:")
print(*mylist)

#to delete last element
print("\nDeleting last element:")
mylist.pop()
print(*mylist)

#to delete second element
print("\nDeleting 2nd element:")
mylist.pop(1)
print(*mylist)

#to delete 23
print("\nTo delete 23 from the list:")
mylist.remove(23)
print(*mylist)

#to remove all items from a list
mylist.clear()
print("\nThe list has been cleared",mylist)




