list1 = [1,2,3,4,5,6,7,8,9]
# substituting
list1[:5] = [2,3,1,2]
# replace every 3rd element
list1[::3] = [1]
# replace and resize
list1[:5] = [1,2,3]
# deleting elements
del list1[2:]