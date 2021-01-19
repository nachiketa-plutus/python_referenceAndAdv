# Use of defaultdict to resolve KeyError

from collections import defaultdict 

# Function to return a default predefined value for 
# a key that does not exist. 

def default_value(): 
	return "The key is not present. Enter a valid input."
	
# Defining the dict 
d = defaultdict(default_value) 
d["a"] = 1
d["b"] = 2

print(d["a"]) 
print(d["b"]) 
print(d["c"]) 
