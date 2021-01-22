# Python program invoking a method using super() 

import abc # Importing Abstract Base Class Module for defiing ABC.
from abc import ABC, abstractmethod 

class Abstr(ABC): 
	def AbMethod(self): 
		print("This is done to print Abstract Base Class") 

class Abstr1(Abstr): 
	def AbMethod(self): 
		super().AbMethod() 
		print("To print subclass ") 

Abstr = Abstr1() 
Abstr.AbMethod() 
