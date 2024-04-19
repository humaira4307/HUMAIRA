
my_list = [1, 2, 3, 4, 5]

my_list.append(6)
print(my_list)

my_list.extend([7, 8, 9])
print(my_list)  

my_list.insert(2, 10)
print(my_list)

my_list.remove(5)
print(my_list)

popped_element = my_list.pop()
print(popped_element)  
print(my_list)


index = my_list.index(3)
print(index)  

count = my_list.count(10)
print(count)  

my_list.sort()
print(my_list)

my_list.clear()
print(my_list)  


