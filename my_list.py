# 1. Creating an empty list
my_list = []  

# 2. Appending elements to my_list: 10, 20, 30, 40
my_list.append(10)  
my_list.append(20) 
my_list.append(30)  
my_list.append(40)
print("After appending elements:", my_list) 

# 3. Inserting the value 15 at the second position in the list
my_list.insert(1, 15) 
print("After inserting 15:", my_list) 

# 4. Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])  # Adds multiple elements to the end of the list
print("After extending:", my_list) 

# 5. Removing the last element from my_list
del my_list[-1] 
print("After removing last element:", my_list) 

# 6. Sorting my_list in ascending order
my_list.sort()   
print("After sorting:", my_list)  

# 7. Printing the index of the value 30 in my_list
index_of_30 = my_list.index(30) 
print("Index of value 30:", index_of_30)   
