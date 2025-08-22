#Count method to count the number of elements in the list
a = (1,45, 352, 3424, False, "rohan", "shivam") 
print(type(a)) 

no = a.count(45) #To find the no/element/variable in the tuple and also show the amount of tiimes it has appeared in the tuple
print(no)

#Index method to find the position 
i = a.index(45) #To find the position of the element/variable in the tuple
print(i) 

#List of Name-Age Pairs
people = [("Rohan", 21), ("Shivam", 22), ("Rita", 23)]
for people, age in people:
    print(people, age)

