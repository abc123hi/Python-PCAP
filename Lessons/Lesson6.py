'''
6.0 Basic Strings in Python
 - create and manipulate strings
 - use string indexing and slicing
 - calculate string length
 - test string membership
 - concatenate strings
 - handle escape characters
 - use raw and unicode string literals
 - compare strings
 - utilize various string methods
'''

'''
6.1 Creating Strings
 - Simple strings are sequences of characters in Python. They can be created by enclosing characters
 in these ''  or these "".
 - Multiline Strings: For strings that span multiple lines, use triple quotes (""") or singles.
'''
# Example 6.1
# Create a simple string
first_name = 'Jillur'
print(first_name)

'''
6.2 Indexing and Slicing
 - Indexing: Access individual characters in a string using their position(index) with the first character
 at index 0.
 - Slicing: Extract a substring by specifying a range of indeces. The syntax is 'string(start:end).'
 Start is inclusive and end is exclusive.
'''

'''
6.3 String Length
 - Length of a string: use the 'len()' function to determine the number of characters in a string
 includes spaces and punctuation.
'''

'''
6.4 String Membership
 - Membership Operators: Use the 'in' keyword to check if a substring exists within a string. This returns True if the
 substring is found and False otherwise.
'''

'''
6.5 Concatenating Strings
 - String Concatenation: Use the '+' operator to join two or more strings into a single string.
'''

'''
6.6 Escape Characters
 - Escape Characters: Use backslash to include special characters in a string,
 such as quotes of newlines characters.
'''

'''
6.7 Raw and Unicode String Literals
 - Raw strings: prefix a string with 'r' to create a raw string where escape characters are not processed.
 - Unicode strings: Prefix a string with 'u' to create a unicode string(neccessary for Python 3)
 but all strings in Python 3 are unicode.
'''

'''
6.8 Comparing Strings
 - Strings comparison: Use comparison operators('==', '!=', '<', '>', '>=', '<=') to compare
 strings lexicographically on their ASCII values.
'''

'''
6.9 String Methods
 - String Methods: Python provides a variety of built-in methods for string manipulation, such as
 lower(), upper(), strip(), replace(), find(), startswith(), endswith(), split(), and join().
'''




# Activities
#1
a = "Derrick Jin"
b = "132977"
print(a)
print(b)
#2
x = "The quick brown fox jumps over the lazy dog."
print(x[4])
print(x[4:9])
print(x[40:43])
#3
c = "Hello world!"
print(len(c))
#4
aa = "b"
if 'b' in aa:
    print('found')
else:
    print('not found')
#5
string1 = "Hello "
string2 = "world!"
string3 = string1 + string2
print(string3)
#6
c = "\abcdefg\""
print(c)
#7
z = r"abc"
v = u"abc"
print(z)
print(v)
#8
stringA = "abc"
stringB = "abc"
if stringA == stringB:
    print("success")
else:
    print("Fail")
#9
my_string = "Hello World!"
print(my_string.lower())
print(my_string.upper())
print(my_string.strip())
print(my_string.replace(my_string, stringA))
print(my_string.find("e"))
print(my_string.startswith('H'))
print(my_string.endswith('!'))
print(my_string.split("Hello"))
bb = ["a","b","c"]
print(" ".join(bb))
