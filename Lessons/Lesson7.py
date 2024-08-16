'''
Understanding Loops in Python
 - While Loops
 - For Loops
 - utilize the range function in loops
 - else keyword
 - nested loops
 - break and continue keywords
'''

'''
7.1 While Loops
 - A while loop repeatedly executs a block of code as long as a specified condition is true.
'''
# Example 7.1
n = int(input("Please enter a positive integer value:  "))    # typecast one data type to another
print(n)
if n < 1:
    print("Please enter a positive number.")
else:
    factorial = 1
    counter = 1
    while counter <= n:
        factorial  *= counter
        counter += 1
    print(f"The factorial of {n} is {factorial}.")

'''
7.2 While-else Loop
 - A while-else loop executes the else block if the while loop completes normally(the condition becomes false.)
'''
# Example 7.3
counter = 1
sum = 0
while counter <= 10:
    sum += counter
    counter += 1
else:
    print(f"The sum of first 10 positive integer values is {sum}.")

'''
7.3 For Loops
 - A for loop iterates over a sequence(tuple, lists, strings, dictionaries) and
 executes a block of code fo each element.
'''
# Example 7.3
shopping_list = ['Apple', 'Banana', 'Butter']
for shopping_item in shopping_list:
    print(f"{shopping_item}: {len(shopping_list)}")

'''
7.4 Range Function
 - The range function generates a sequence of numbers which is commonly used in for loops.
'''
#Example 7.4.1
# Range function with single argument
# prints 0 - 9
for n in range(10):
    print(n)
#Example 7.4.2
# Range function with two argument
# prints 10 - 19
for n in range(10,20):
    print(n)
#Example 7.4.3
# Range function with three argument
# print 10 - 18
for n in range(10,20,2):
    print(n)
'''
7.5 For-else Loops
 - A for-else loop executes the else block if the for loop executes normally(without encountering a break statement).
'''
# Example 7.5
for n in range(3):
    password_attempt = input('Please enter your password:  ')
    if password_attempt == "Passw0rd123!":
        print('Successful authentication.')
        break
else:
    print('Your account has been locked.')

'''
7.6 Break Statement
 - The break statement terminates the loop prematurely.
'''
# Example 7.6
import random
random_n = random.randint(1,30)
guess_counter = 0
guess_l = 5
print("******** Guess the Number! ********")
print(f"I am thinking of a number between 1 and 30. Can upi guess it in less than {guess_l} attempts?")
while guess_counter < guess_l:
    guess = int(input(f"Attempt #{guess_counter + 1} Enter your guess:  "))
    guess_counter += 1
    if guess < random_n:
        print("Too low!")
    elif guess > random_n:
        print("Too high!")
    else:
        break
if guess == random_n:
    print(f"Congratulations! You guessed correctly in {guess_counter} attempts!")
else:
    print(f"Sorry! Game over! The number I was thinking of was {random_n}.")

'''
7.7 The Continue Statement
 - The continue statement skips the rest of the code inside the loop for the current iteration and
 moves to the next iteration.
'''
# Example 7.7
shopping_list = ['Apple','Bananas','Potatoes','Tomatoes','Milk','Cheese']
dairy_products = ["Milk","Cheese"]
for shopping_item in shopping_list:
    if shopping_item in shopping_list:
        continue
    print(shopping_item)

'''
7.8 Nested Loops
 - Nested loops are loops inside loops. Each time the outer loop runs, the inner loop runs completely.
'''
# Example 7.8
number_columns = 5
number_rows = 5
fill_character = "*"
for row in range(number_rows):
    print(fill_character,end=" ")
    for column in range(number_columns - 1):
        print(fill_character, end=' ')
    print('')
'''
Explanation:
The outer loop runs for each row.
The inner loop runs for each column.
The end=' ' parameter in print keeps the cursor on the same line.
The rectangle is printed with specified dimensions.
'''

'''
8 Advanced Strings in Python
 - Understand and use character encodings
 - Utilize escape characters
 - Explain and handle immutable strings
 - Work with multi-line strings
 - Compare string effectively
 - Slicing/cloning techniques
 - common string methods and functions
'''

'''
8.1 Character Encoding
 - Character encodings are methods of converting characters into bytes and vice versa.
 Unicode is the most common encoding used in Python.
'''

'''
8.2 Escape Sequences
 - Escape sequences allow the inclusion of special characters in strings.
'''

'''
8.3 Immutable Strings
 - Strings in Python are immutable, meaning they cannot be changed after they are created.
'''
# Example 8.3.1
test_string = 'Hello World'
print(test_string[6])
test_string[6] = "a"
# Example 8.3.2

'''
8.4 Multi-Line Strings
 - Multi-line strings are created using triple quotes.
'''
# Example 8.4

'''
8.5 String Comparision
 - Strings can be compared using comparison operators.
'''

'''
8.6 Advanced String Slicing
 - String slicing allows extracting parts of a string using syta 'string[start:end:step].'
'''

'''
8.7 Copying and Cloning
 - Strings can be copied or cloned using slicing.
'''

'''
8.8 String Methods
'''

'''
8.9 String Functions
'''