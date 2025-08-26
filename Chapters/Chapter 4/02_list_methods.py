#Appending elements to a list
# This code snippet demonstrates how to append elements to a list in Python.
friends = ["Apple","Orange", 5, 345.06, False, "Hriday", "Scout"] 
print(friends) 

friends.append("Yashvi")  # Adding an element to the end of the list #Append = adding any element to the end of the list
print(friends) 

#Sorting a list
# This code snippet demonstrates how to sort a list in Python.
l1 = [0, 88, 944, 5, 98, 44] 
l1.sort()  # Sorting the list in ascending order
print(l1) 

#Reversing a list {doesnt sort the list, just reverses the order of elements you have entered}
# This code snippet demonstrates how to reverse a list in Python.
l2 = [0, 88, 944, 5, 98, 44] 
l2.reverse()  # Reversing the order of elements in the list
print(l2)

#Inserting elements at a specific position  {Can be used to insert any element at any position in the list}
# This code snippet demonstrates how to insert an element at a specific position in a list in Python.
l3 = [0, 88, 944, 5, 98, 44] 
l3.insert(2, "Hriday")  # Inserting "Hriday" at index 2
print(l3)

#popping elements from a list
# This code snippet demonstrates how to pop (remove) an element from a list in Python.
l4 = [0, 88, 944, 5, 98, 44]
l4.pop(2)  # Popping the last element from the list
print(l4) 

print(l4.pop(2))  # Popping the element at index 2 and printing it stand alone
print(l4)  # Printing the list after popping the element makes it clear that the element has been removed

value = l4.pop(2)  # Popping the element at index 2 and storing it in a variable
print(value)
print(l4)  # Printing the list after popping the element to show the updated list 

#removing elements from a list 
# This code snippet demonstrates how to remove an element from a list in Python.
l5 = [0, 88, 944, 5, 98, 44]
l5.remove(5)  # Removing the first occurrence of 5 in the list 
print(l5)  # Printing the list after removing the element          