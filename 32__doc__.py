def __doc__Function(): 
	'''This is to show demonstration of 
docstrings with triple quotes .'''

	return None

print("With the help of __doc__:") 
print(__doc__Function.__doc__) 

print("With usage of help:") 
help(__doc__Function) 
