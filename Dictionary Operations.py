#Creating a Dictionary
student={'stdid':'std101','stdname': 'Ashish Kumar','standard': '10th','age': 15}
print("Dictionary is ",student)

#insert element with key standard
print("\nInsert a different element in key 'standard' in student dictionary: ")
student['standard']='12th'
print(student)

#insert an element with key hindi
print("\nInsert element with key hindi in student dictionary: ")
student['hindi']=78
print(student)

#find the key of dictionary
print("\nKeys in student dictionary are:")
for key in student:
  print(key)
  
#print the value of dictionary with it's key
print("\nElements of dictionary in (key:value) pair:")
for key in student:
  print(key,":",student[key])


#delete element having key as hindi
print("\nRemoving the element from dictionary having key as hindi :")
student.pop('hindi')
print(student)

#To delete the last item in dictionary
print("\nRemoving the last item from a dictioary:")
student.popitem()
print(student)

#Using keys() to return the keys of all the element in List
print("\nDisplay the list of keys in List:")
element_keys=student.keys()
print(element_keys)

#Using values() to return the values of all the element in List of a Dictionary
print("\nDisplay the list of values in List:")
element_values=student.values()
print(element_values)

#Using items() to return the a list of items
print("\nDisplay the list of item of a dictionary in List")
dict_items=student.items()
print(dict_items)

#To find all the value of all the element
print("\nDisplay the values of all key of a Dictionary: ")
for data in student.values():
  print(data)

#using get() to check the whether key is available in a dictionary or not
print("\nIs key (maths) is available in dictionary?  ")
x= student.get('maths')
print(x)

# Using update()
dict1={'name':'Amit','Age':15,'standard':'10th'}
print("\nDictionary1 is: ",dict1)
dict2={'hindi':67,'Age':16,'standard':"12th",'English':67}
print("Dictionary2 is: ",dict2)

# inserting all the element of the dict2 into dict1
print("\nInserting all the element of the dictionary2 into dictionary1: ")
dict1.update(dict2)
print(dict1)

#Using fromkeys()
print("\nUsing fromkeys method in dictionary1 in key 'english':")
x=dict1.fromkeys('english',16)
print(x)

print("\nUsing fromkeys method in dictionary1 in it's keys and values: ")
y=dict1.fromkeys(dict1.keys(),dict1.values())
print(y)

print("\nUsing fromkeys method in dictionary1 in it's keys and using value '16':")
z=dict1.fromkeys(dict1.keys(),16)
print(z)

#Using len() to find the no. of element of a dictionary
print("Length of the dictionary1 is :")
print(len(dict1))
