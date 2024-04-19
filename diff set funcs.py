my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(3)
my_set.discard(7) 
popped_element=my_set.pop()

another_set = {4, 5, 6, 7, 8}

copied_set = another_set.copy()

my_set.update(another_set)

intersection_set = my_set.intersection(another_set)

union_set = my_set.union(another_set)

difference_set = my_set.difference(another_set)
clear_set=my_set.clear()

print("Modified Set:", my_set)
print("Popped Element:", popped_element)
print("Copied Set:", copied_set)
print("Intersection Set:", intersection_set)
print("Union Set:", union_set)
print("Clear Set:",clear_set)
print("Difference Set:", difference_set)