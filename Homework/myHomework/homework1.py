import math
def calc_area(r):
    return math.pi * r ** 2
print(calc_area(5))
list1 = [1,5,3]
list1.sort()
print(list1)
a = input('Enter your Name:  ')
x = float(input('Test score 1:'))
y = float(input('Test score 2:'))
z = float(input('Test score 3:'))
b = x+y+z / 3
print('Hello,',a,'. Your test average is',b,'.')
def invalid_inputs(x):
    if x == str:
        print("invalid input")
print(invalid_inputs(x))
c = float(input('Enter your salary:  '))
print(f"Hello",a,"Your salary is $",c)
format(c)
bb = int(input("Enter a number: "))
if bb == 0:
    print('0')
if bb < 0:
    print('neg')
if bb > 0:
    print('pos')
# didn't know how to do the prime number
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
list2 = ['the lego movie', 'the lego movie 2', 'lego ninjago movie', 'movie 1', 'movie 2']
list2.insert(1,"movie 3")
del list2[3]
def even_ban(x):
   for i in x():
        if 1 % 2 == 0:
             del i
print(list2[1:4])
list2.insert(-1,"best movie")
list2.pop(2)
print(list2.pop(4))
list2.count('the lego movie 2')
list3 = ['the lego movie', 'the lego movie','the lego movie 2','the lego movie']
list3.count('the lego movie')
list12 = list2 + list3
list12.sort()
list12.sort(reverse=True)
list12.reverse()
list12[:4].reverse()
print(list12)