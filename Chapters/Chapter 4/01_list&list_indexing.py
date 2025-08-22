friends = ["Apple","Orange", 5, 345.06, False, "Hriday", "Nishtha"]
print(friends[6])  # Accessing elements by index

friends[0] = "Dragonfruit"  # Modifying an element #Unlike strings, lists are mutable
print(friends[0])
friends[6] = "Nishtha Dedhia"  # Modifying another element
print(friends[6]) 
 
 #Indexing and slicing in lists
print(friends[0:4])  # Slicing the list to get first four elements
print(friends[1:])  # Slicing the list to get elements from index 1 to the end
print(friends[:3])  # Slicing the list to get first three elements 