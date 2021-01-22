# Python program creating context manager 

class ContextManager(): 
	def __init__(self): 
		print('init method has been called') 
		
	def __enter__(self): 
		print('enter method has been called') 
		return self
	
	def __exit__(self, exc_type, exc_value, exc_traceback): 
		print('exit method has been called') 


with ContextManager() as manager: 
	print('this is alongside the statement block') 
