a = 31  
t = type(a)  # Get the type of a i.e. integer

print(t)  # This will print <class 'int'>

b = 3.14
t = type(b)  # Get the type of b i.e. float     

print(t)  # This will print <class 'float'>

c = "Hriday loves Nishtha!"
t = type(c)  # Get the type of c i.e. string    

print(t)  # This will print <class 'str'>

d = "28.19"
t = type(d)  # Get the type of d i.e. string (even though it looks like a float)

print(t)  # This will print <class 'str'>

e = "28.19"
f = float(e)  # Convert string to float
t = type(f)  # Get the type of f i.e. float 

print(t)  # This will print <class 'float'>