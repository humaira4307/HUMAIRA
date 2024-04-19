my_dict = {'a': 1, 'b': 2, 'c': 3}

print("Keys:", my_dict.keys())     
print("Values:", my_dict.values()) 
print("Items:", my_dict.items())   

print("Value for key 'a':", my_dict.get('a'))  
print("Value for key 'd':", my_dict.get('d', 'Key not found')) 

my_dict.update({'d': 4})  
print("Updated Dictionary:", my_dict)  

print("Removed item:", my_dict.pop('a'))  
print("Dictionary after popping 'a':", my_dict)  

print("Popped item:", my_dict.popitem()) 
print("Dictionary after popping an item:", my_dict)  

my_dict.clear()  
print("Cleared Dictionary:", my_dict) 