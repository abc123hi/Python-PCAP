# 1. for loops iterate by a variable, while while loops use True or False.
for x in range(1,10):
    print(x)
# while True:
#     print(True)

# 2. Write a function definition for a function that takes two arguments, a string and a character,
#  and returns the number of times the character appears in the string.
def function1(a,b):
    counter = 0
    for b in a:
        counter +=1
        print(counter)
function1('aaa','a')

# 3. A nested loop is a loop in a loop.
for i in range(1,12):
    for i in range(1,6):
        print(i)

# 4. break: ends loop
# 4.1. continue: end current iteration
while True:
    break
while True:
    continue

# 5. List comprehension is the process of creating a list based on an existing list.
list1 = [n for n in numbers if n % 2 == 0]
print(list1)

# 6. Mutable: can be changed, Immutable: unchangable
mutable = [1,2,3]
immutable = frozenset[1,2,3]
