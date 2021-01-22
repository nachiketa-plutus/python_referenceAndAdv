# To demonstrate the use of @property decorator 

class Celsius: 
	
	# Initializinf parameter using init method
	def __init__(self, temp = 0): 
		self._temperature = temp 

	# Beginning of the @property decorator 
	@property
	
	# Getter method 
	def temp(self): 
		 
		print("The value of the temperature is: ") 
		return self._temperature 

	# Setter method 
	@temp.setter 
	def temp(self, val): 
		 
		if val < -273: 
			raise ValueError("The value of the temperature entered throwed a value error.") 
		else: 
		    print("The value of the tempereture is set.") 
		self._temperature = val 


# Creating object for the stated class 
cel = Celsius()

# Setting the temperature value 
cel.temp = -270

# Prints the temperature that is set 
print(cel.temp) 

''' Setting the temperature value to below the specified range 
-300 which is not possible to throw an error
thrown''' 

cel.temp = -300
