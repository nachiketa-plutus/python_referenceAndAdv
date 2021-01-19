# A class with init method 
class Nachiketa: 
	
	# init method or constructor 
	def __init__(self, MyName): 
		self.MyName = MyName 
	
	# Sample Method 
	def hello(self): 
		print('Hello, I am known as', self.MyName) 

# Creating different objects	 
p1 = Nachiketa('Nachiketa') 
p2 = Nachiketa('Abhiraj') 
p3 = Nachiketa('Anchal') 

p1.hello() 
p2.hello() 
p3.hello() 
