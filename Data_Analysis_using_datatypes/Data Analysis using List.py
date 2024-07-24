from tabulate import tabulate

# Creating student dataset using List
data = [
    ["std101", "Ashish Kumar", "10th", 15, 67, 89, 87, 89, 90, 422],
    ["std102", "Abhishek Kumar", "10th", 14, 85, 45, 48, 90, 45, 313],
    ["std103", "Aman", "10th", 15, 23, 56, 78, 78, 67, 302],
    ["std104", "Rahul", "10th", 14, 45, 67, 45, 45, 56, 258],
    ["std105", "Ruby", "10th", 13, 89, 67, 89, 93, 65, 403],
    ["std106", "Suman", "10th", 13, 90, 46, 67, 67, 67, 337],
    ["std107", "Saurabh", "10th", 15, 45, 23, 34, 45, 34, 181],
    ["std108", "Sumit", "10th", 14, 23, 45, 67, 78, 90, 303],
    ["std109", "Kamlesh", "10th", 15, 45, 56, 78, 99, 67, 345],
    ["std110", "Rohan", "10th", 15, 34, 12, 24, 45, 56, 171]
]

# Define the headers
headers = ["stdid", "stdname", "standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"]

# Display the table
print("Student dataset in table:")
print(tabulate(data, headers=headers, tablefmt="grid"))
print( )
# Define the index for English marks
english_index = 5

# Find and print the names of students with English marks greater than 50 using a for loop
print("Students with English marks greater than 50:")
for row in data:
    if row[english_index] > 50:
        print(row[1])
        

print("\nName and Age of a student who are top four scorer in Maths:")
relevant_data = [(row[1], row[3], row[6]) for row in data]   # Extracting student name, age, and Maths score
sorted_data = sorted(relevant_data, key=lambda x: x[2], reverse=True)    # Sorting the data by Maths score in descending order
top_four = sorted_data[0:4]    # Selecting the top four students
for student in top_four:
    print("Student Name:" ,student[0],", Age:", student[1])    

print("\nName, Id and Age of student who are bottom three scorer in Computer:")
relevant_data = [(row[0], row[1],row[3], row[8]) for row in data]   # Extracting student id,name, age, and computer score
sorted_data = sorted(relevant_data, key=lambda x: x[3])     # Sorting the data by computer score in ascending order
bottom_three = sorted_data[0:3]    # Selecting the bottom three students
for student in bottom_three:
    print("Student Id: ",student[0],", Student Name:", student[1],", Age:", student[2])
