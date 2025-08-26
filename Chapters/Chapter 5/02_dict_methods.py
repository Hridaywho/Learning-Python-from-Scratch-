marks = {
    "Nishtha": 95,
    "Hriday": 85,
    "Riddhi": 80,
    0: "Nishtha"
} 

# a.items() method : Returns a list of (key,value)tuples.
print (marks.items())

#a.keys() method : Returns a list containing dictionary's keys.
print (marks.keys())

#a.values() method : Returns a list of dictionary's values.
print (marks.values())

# a.update({"friends":}): Updates the dictionary with supplied key-value pairs.
marks.update({"Hriday": 90})
print(marks)
# As dictionary is mutable, we can update it. 
#so we can change the value of an existing key or add a new key-value pair. 

#a.get()method #Difference is asked between the following two statements print ([marks["Riddhi"]) AND print(marks.get("Riddhi"))
#the difference is the .get would return None if the key doesn't exist, while the [] would raise an error.
#this is asked in interviews so important
print(marks.get("Riddhi")) 
#By this we can get the specific value of the person or key by writing the keywords and using the following code to help us.

#dict.pop() method: Removes the specified key and returns the corresponding value.
print(marks.pop("Riddhi"))
print(marks)

#a.popitem() method: Removes and returns the last inserted key-value pair as a tuple.
print(marks.popitem()) 

