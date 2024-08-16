# sample 2d list
list2d = [[1,2],[1,2]]
# accessing
for i in list2d:
    if i == 2:
        print('accessed')
# 2d array with list comprehension
list1 = [[num * num for num in range(1,9)],[num * num for num in range(1,9)]]
# update, insert, delete, and append
list1[1][0] = 3
list1.insert([1][0],3)
del list1[1]
list1.append(12)
# 3d array manipulation
a = [[[1,2]],[[1,2]]]
a[0][0][0] = 3