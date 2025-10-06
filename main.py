list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list(map(lambda x: (x[0] ** 2, x[1] ** 3), list(zip(list1, list2))))
print(result)
