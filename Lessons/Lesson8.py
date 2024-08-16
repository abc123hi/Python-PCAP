'''
9 Advanced Lists in Python
 - Access and manipulating list elements using indexing and slicing.
 - Understand and apply advanced list slicing techniques.
 - Differentiate between shallow and deep copies of list
 - Multi_dimensional arrays.
'''

'''
9.1 Index and Negative Indexing
 - Lists in Python can be accessed by using index numbers. Negative indexing allows access to elements from the
 end of the list.
'''
# Example 9.1
# Create a list containing the first ten squares.
squares = [1,4,9,16,25,36,49,64,81,100]

'''
9.2 Advanced List Slicing
 - List slicing allows you to use sytax 'list[start:end]'
'''
# Example 9.2.1
# Extract elements from a list using the stride size argument.
print(squares[::2])
# Example 9.2.2
# Use negative indexing using the stride size argument.
print(squares[::-2])
# Example 9.2.3
# Extract elements at a defined set of known as a subset.
print(squares[4:8:2])
# Example 9.2.4
# Extract elements with even indexes from the 5th element.
print(squares[4::2])

'''
9.3 Advanced List Assignment
 - Lists can be modified by assigning values to slices of the list.
'''
# Example 9.3
my_numbers = [1,3,6,10,15,21,28,36,45,55]
print(f'My list of numbers (first 10 triangle numbers): {my_numbers}')
my_numbers[1:3] = [4,9]
print(f'my list of numbers (substitions): {my_numbers}')
my_numbers[::3] = [1,16,49,100]
print(f'My list of numbers (n-th replacement): {my_numbers}')
my_numbers[4:] = [25,36,49,64]
print(f'My list numbers (first 8 squares): {my_numbers}')
del my_numbers[1::2]
print(f'My list of numbers (every other square number): {my_numbers}')

'''
9.4 Shallow and Deep List Copies
 - Shallow copies duplicate the structure of a list but not the elements of the list.
 - Deep copies duplicate both structure and elements. 
'''
# Example 9.4
my_phrases = [['a','b','c'],['d','e','f'],['g','h','i']]
my_shallow_phrases = my_phrases[:2] + [['j','k','l']]
my_other_shallow_phrases = list(my_phrases) + [['j','k','l']]
my_phrases[0][0] = 'ALPHA'
my_phrases[0][1] = 'BETA'
my_phrases[0][2] = 'GAMMA'
import copy
my_deep_phrases = copy.deepcopy(my_phrases)
my_phrases[0][0] = 'ALPHA'
my_phrases[0][1] = 'BETA'
my_phrases[0][2] = 'GAMMA'

'''
9.5 Iterating List
 - Lists can be iterated through using while loops, for loops, and the enumerate function.
'''
# Example 9.5
my_diatomic_list = [0,1,1,2,1,3,2,3,1,4,3,5,2,5,3,4,]
i = 0
while i <len(my_diatomic_list):
    print(f'Diatomic Sequence - Element #{i + 1}: {my_diatomic_list[i]}')
    i += 1
for elem in my_diatomic_list:
    print(elem)
for idx, elem in enumerate(my_diatomic_list):
    print(f'Diatomic Sequence - Element # {idx + 1}: {elem}')

'''
9.6 List Membership
 - List membership can be tested using the 'in' and 'not in' operators.
'''
squares = [1,4,9,16,25]
x = 16
if x in squares:
    print(True)
else:
    print(False)
y = 169
if y not in squares:
    print(True)
else:
    print(False)

'''
9.7 List Comprehension
 - List comprehension provides a conscise way of creating lists.
'''
# Example 9.7
squares = [num * num for num in range(1,9)]
print(squares)
letters_in_abibliophobia = [character for character in 'abibliophobia']
print(letters_in_abibliophobia)
even_numbers_zeroed_odds = [i if i % 2 == 0 else 0 for i in range(1, 101)]
print(even_numbers_zeroed_odds)

'''
9.8 Multi-Dimensional Arrays
 - List that contains other lists
'''
# Example 9.8
my_2d_array = [[1,2,3],[1,2,3]]
