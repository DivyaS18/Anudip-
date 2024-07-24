#Q1) Write a Python program to Count all letters, digits, and special symbols from the given string

def count_characters(input_string):
    letters = 0
    digits = 0
    symbols = 0

    for char in input_string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif not char.isspace():  # Counts anything that is not a space as a symbol
            symbols += 1

    return letters, digits, symbols

input_string = "P@#yn26at^&i5ve"      # Given input string
chars, digits, symbols = count_characters(input_string)       # Count the characters

print("Displaying the count of all letters, digits and special symbols from the string 'P@#yn26at^&i5ve'")    # Displaying the results
print(f"Chars = {chars}")       
print(f"Digits = {digits}")
print(f"Symbols = {symbols}\n")


print("-------*---------*--------*---------*-------*---------*--------*---------*---------")


#Q2) Write a Python program to remove duplicate characters of a given string.

def remove_duplicate_words(input_string):
    words = input_string.split()  # Splitting the input string into words
    seen = set()  # To keep track of seen words
    result = []  # To store the processed words

    for word in words:
        if word not in seen:
            seen.add(word)  # Adds word to the set
            result.append(word)  # Adds word to the result list

    return ' '.join(result)  # Joining the processed words back into a single string

input_string = "String and String Function"  # Given input string
output_string = remove_duplicate_words(input_string)  # Removing duplicate words
print("Removing duplicate words from the string 'String and String Function'")
print(f"Output: {output_string}")  # Displaying the output string



print("-------*---------*--------*---------*-------*---------*--------*---------*---------")


#Q3) Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string

input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"   # Given input string

uppercase_count = 0        # Initializing counters
lowercase_count = 0
numeric_count = 0
special_count = 0

for char in input_string:              # Iterate through each character in the string
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        numeric_count += 1
    elif not char.isalpha():  # Consider anything that is not a letter (including spaces) as special
        special_count += 1

print("\nDisplaying the count of Uppercase, Lowercase, special character and numeric values in the string 'Hell0 W0rld ! 123 * # welcome to pYtHoN'") 
print(f"UpperCase : {uppercase_count}")        # Displaying the counts
print(f"LowerCase : {lowercase_count}")
print(f"NumberCase : {numeric_count}")
print(f"SpecialCase : {special_count}")


print("-------*---------*--------*---------*-------*---------*--------*---------*---------")



#Q4) Write a Python Count vowels in a string

input_string = "Welcome to Python Assignment"       # Given input string
vowels = "aeiouAEIOU"       # Defining the vowels
vowel_count = 0     # Initializing the vowel count

for char in input_string:                    # Iterating through each character in the string
    if char in vowels:
        vowel_count += 1

print("\nDisplaying the count of vowels in the string 'Welcome to Python Assignment'")
print(f"Total vowels are: {vowel_count}")    # Displaying the count of vowels








