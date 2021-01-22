# ChainMap encapsulates many dictionaries into one unit. Part of collections module. 
	
	
from collections import ChainMap 
	
Ex1 = {'a': 1, 'b': 2} 
Ex2 = {'c': 3, 'd': 4} 
Ex3 = {'e': 5, 'f': 6} 
	
# Defining the chainmap 
ChainMap1 = ChainMap(Ex1, Ex2, Ex3) 
	
print(ChainMap1) 
