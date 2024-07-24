#Q1) Write a Python program to count the occurrences of each word in a given sentence

from collections import Counter
import re

def count_word_occurrences(sentence):
    sentence = sentence.lower()          # Converting the sentence to lowercase to ensure case insensitivity
    words = re.findall(r'\b\w+\b', sentence)        # Removimg punctuation and split the sentence into words
    word_counts = Counter(words)            # Counting the occurrences of each word
    return word_counts

sentence = "To change the overall look of your document. To change the look available in the gallery"          # Given input sentence
word_counts = count_word_occurrences(sentence)             # Counting the occurrences of each word
print("Displaying the count of each word in a given sentence: ")
for word, count in word_counts.items():               # Displaying the word counts
    print(f"'{word}': {count}")

print("-------*---------*--------*---------*-------*---------*--------*---------*---------")


#Q2)Write a Python program to remove a newline in Python

input_string = "\nBest \nDeeptech \nPython \nTraining\n"      # Given input string
cleaned_string = input_string.replace('\n', '')          # Removing newline characters
print("\nRemoving the newline from the given string:",input_string)
print(f"The cleaned String is: '{cleaned_string}'")         # Displaying the result


print("-------*---------*--------*---------*-------*---------*--------*---------*---------")


#Q3)Write a Python program to reverse words in a string

def reverse_words(input_string):
    words = input_string.split()      # Spliting the string into words
    reversed_words = words[::-1]      # Reversing the order of words
    return ' '.join(reversed_words)     # Joining the reversed words back into a single string

input_string = "Deeptech Python Training"     # Given input string
reversed_string = reverse_words(input_string)    # Reversing the words in the string
print("\nThe string to be reversed is: ",input_string)
print(f"The reversed words in the string are : {reversed_string}")    # Displaying the result

print("-------*---------*--------*---------*-------*---------*--------*---------*---------")


#Q4) Write a Python program to count and display the vowels of a given text

def count_and_display_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = {v: 0 for v in vowels}  # Initializing a dictionary to keep track of each vowel's count

    for char in text:
        if char in vowels:
            vowel_count[char] += 1

    for vowel, count in vowel_count.items():       # Displaying the counts of each vowel
        if count > 0:
            print(f"'{vowel}': {count}")

text = "Welcome to python Training"          # Given input string
print("\nDisplaying the count of vowels in the given text: ",text)
count_and_display_vowels(text)         # Count and display the vowels in the string




