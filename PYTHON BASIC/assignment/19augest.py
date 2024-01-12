# Task 1: Swap values of two variables without using a temporary variable
a = 6
b = 9
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)

# Task 2: Calculate the area of a rectangle
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
area = length * breadth
print("Area of rectangle is", area)

# Task 3: Convert temperatures from Celsius to Fahrenheit
celsius_temperature = float(input("Enter temperature in Celsius: "))
fahrenheit_temperature = (celsius_temperature * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit_temperature)


# STRING BASED TASKS

# Task 1: Print the length of a string
string_input = input("Enter any string: ")
print("Length of the string:", len(string_input))

# Task 2: Count the number of vowels in a string
string_input = input("Enter any string: ")
vowel_count = 0
for char in string_input:
    if char.lower() in "aeiou":
        vowel_count += 1
print("Total vowels in the string:", vowel_count)

# Task 3: Reverse the order of characters in a string using string slicing
string_input = input("Enter any string: ")
reversed_string = string_input[::-1]
print("Reversed string:", reversed_string)

# Task 4: Check if a string is a palindrome
string_input = input("Enter any string: ")
if string_input == string_input[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Task 5: Remove spaces from a string
string_input = input("Enter any string: ")
string_without_spaces = string_input.replace(" ", "")
print("Modified string without spaces:", string_without_spaces)
