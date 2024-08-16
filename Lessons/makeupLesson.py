'''
(12)Functions, (10)Tuples, and (11)Dictionaries
 - Understanding the basics of a function
 - Explore advanced usages of functions with tuples and dictionaries
'''

'''
Intro to Functions
'''
def function_name():
    '''
    Docstring(optional)
    '''
    print("my function is used")
function_name()
print(function_name.__doc__)

# parameters
def add(x,y):
    return x + y
print(add(5,7))

# default parameters
def get_name(name='Jillur'):
    print(name)
get_name()

# keyword args
print(add(y = 7, x = 10))

# Lambda functions
add_lambda = lambda x,y: x+y
print(add_lambda(2,9))

'''
Tuples
'''
# returning tuples from functions
def calc_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count != 0 else 0
    return total,count,average
# call the function
stats = [10,20,30,40]
my_results = calc_stats(stats)
print(my_results)
# return dictionary
def analyze_text(text):
    word_count = len(text.split())
    char_count = len(text)
    unique_words = len(set(text.split()))
    return {
        "word_count": word_count,
        "char_count":char_count,
        "unique_words":unique_words
    }
text_analysis = analyze_text('aba, basd, abd, qaa, abba')
print(text_analysis)
# Add an item
text_analysis["magic_word"] = "Python"
print(text_analysis)
print(text_analysis["magic_word"])
# delete items
del text_analysis["magic_word"]
print(text_analysis)

def update_inventory(inventory, item_info):
    item, quantity = item_info
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    return inventory

# create a dictionary
inventory = {
    "apples":10,
    "oranges":5
}
# call the function with a tuple
updated_inventory = update_inventory(inventory("apples",10))
print(updated_inventory)