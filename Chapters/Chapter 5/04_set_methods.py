i = {1, 32, 54, 5 ,5, 5, 5, "Harry"}

print(i, type(i))
i.add(566)
print(i, type(i))

i.remove(32)
print(i, type(i))

#_______________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________
 
 # Type of set methods.
#✅ 1. Adding & Removing Elements
# Create a set
s = {1, 2}

s.add(3)               # Adds 3 → {1, 2, 3}
s.remove(2)            # Removes 2 → {1, 3}
s.discard(5)           # No error if 5 not found
elem = s.pop()         # Removes & returns random element
s.clear()              # Now set is empty {}

#✅ 2. Union
a = {1, 2}
b = {2, 3}
print(a.union(b))      # {1, 2, 3}

#✅ 3. Intersection
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}

#✅ 4. Difference
a = {1, 2, 3}
b = {2, 4}
print(a.difference(b))    # {1, 3}

#✅ 5. Symmetric Difference
a = {1, 2, 3}
b = {2, 3, 4}
print(a.symmetric_difference(b))  # {1, 4}   
# Gives elements which are not common in both set A and B.

#✅ 6. Update Methods (In-place)
a = {1, 2}
b = {3, 4}
a.update(b)                   # a = {1, 2, 3, 4}
a.intersection_update({2, 3}) # a = {2, 3}
a.difference_update({3})      # a = {2}
a.symmetric_difference_update({1, 2}) # a = {1}

#✅ 7. Subset / Superset / Disjoint
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))     # True
print(b.issuperset(a))   # True
print(a.isdisjoint({3})) # True