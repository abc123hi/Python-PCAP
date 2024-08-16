# 1
emptylist = []
for i in range(1, 51):
    if i % 2 == 0:
        emptylist.append(i)
sum_of_evens = sum(emptylist)
print(f"The sum of all even numbers between 1 and 50 is: {sum_of_evens}")
# 2
for i in range(1, 6):
  for j in range(i):
    print("*", end="")
  print()
# 3
passw = input('ENter password:  ')
if passw == 'abc123':
   print('Access Granted.')
elif passw != 'abc123':
   print('Access denied.')

# 4
# i dont know

# 5
def isPalindrome(word):
  left = 0
  right = len(word) - 1
  while left < right:
    if word[left] != word[right]:
      return False
    left += 1
    right -= 1
  return True
word = "racecar"
print(isPalindrome(word))
# 6
def vowel(a):
   counter = 0
   for i in a:
      if i == 'a' or 'e' or 'i' or 'o' or 'u':
         counter+=1
         print(counter)
# 7
listcomp = [num*num for num in range(1,11)]
# 8
def common(a, b):
  emptylist = []
  for i in a:
    if i in b:
      emptylist.append(i)
  return emptylist
# 9
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
# 10
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)
# 11
import math
def hypotenuse(a,b):
  return math.sqrt(a ** 2 + b ** 2)
print(hypotenuse(3,4))
# 12
def circ_area(r):
  return math.pi * r ** 2
# 13
def gcd(a):
  math.gcd(a)
# 14
import random
def randomlist(n):
  emptylist = []
  for i in range(1,n+1):
    random.randint(i)
    emptylist.append(i)
  return emptylist
# 15
def exponential(n):
  print(math.exp(n))
  