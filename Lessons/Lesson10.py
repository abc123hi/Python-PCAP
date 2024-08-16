'''
12.6 Function Recursion
Recursion occurs when a function calls itself.
'''
# Calculate the nth element in the fibonacci sequence.
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(10))

'''
12.7 Local Scope Variables
Variables are defined inside a function and are only accessible
inside the function.
'''
def calculate_weight(h,a):
#   sytax: 'global total_weight'
    total_weight = h * a
    print(total_weight)

'''
12.8 Generator Functions
Generator functions use the 'yield' keyword to return a value and suspend their execution,
allowing them to be resumed.
'''
def inf_sequence_gen():
    counter = 0
    while True:
        yield counter
        counter += 1
# Call this generator function and lazily evaluate the next element in the iterable object.
infinite_gen = inf_sequence_gen()
print(next(infinite_gen)) 
print(next(infinite_gen))
print(next(infinite_gen))

for i in range(1,10):
    print(next(infinite_gen))

'''
12.9 Generator Termination
Generators raise a 'StopIteration' exception when there are no further elements to generate.
'''
# Define a generator.
def letter_seq_gen(start,stop,step=1):
    for ord_unicode in range(ord(start.lower()),ord(stop.lower()),step):
        yield chr(ord_unicode)
alphabet = letter_seq_gen('a','e',2)
print(next(alphabet))
print(next(alphabet))

alphabet = letter_seq_gen('a','z')
for letter in alphabet:
    print(letter, end=' ')

'''
12.10 Generator Expressions
Generator expressions are similar to list comprehensions but use parentheses instead of '[]'
'''
# Example 12.10.1
first_million = (num for num in range(1,1_000_000))
print(first_million)
print(next(first_million))
print(next(first_million))
# Example 12.10.2
alphabet = letter_seq_gen("a","2")
alphabet_list = list(alphabet)
print(alphabet_list)

'''
12.11 Lamba Functions
Lambda functions are anonymous functions defined using the 'lambda' keyword. They can have
any number of parameter but only one expression.
'''
# Example 12.11.1
square = lambda n: n*n
print(square(5))
# Example 12.11.2
volume = lambda x,y,z:x * y * z
print(volume(3,10,5))

# Exercise 1.1
tuple1 = (1,'A',12.1)
print(tuple1)
# Exercise 1.2
print(tuple1[1])
# error
# Exercise 1.3
print(tuple1.count(1))
print(tuple1.index(1))
# Exercise 1.4
(a,b,c) = tuple1
print(a)
print(b)
print(c)
# Exercise 2.1
values = {1:'a',2:'b',3:'c'}
print(values)
# Exercise 2.2
print(values[1])
try:
    print(values[125632])
except:
    print('Error')
