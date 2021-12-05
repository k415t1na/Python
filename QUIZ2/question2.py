#Create a function that expects two lists as parameters and returns a new list containing only the unique common elements (the order of the elements in the resulting list is not important).

#Let’s have two lists - list1 = [1, 6, 1, 7, 4] and list2 = [9, 10, 4, 6, 1, 4], the resulting list should be [1, 4, 6]


def sol(l1, l2):
	return list(set(l1).intersection(set(l2)))

print(sol([1, 6, 1, 7, 4],[9, 10, 4, 6, 1, 4]  ))
	