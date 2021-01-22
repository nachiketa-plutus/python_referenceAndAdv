# Representation of enumerated number in different formats
# THe module enum being imported  for enumerations 
import enum 

class Plutus(enum.Enum): 
	employee = 1
	CTO = 2
	Salesman = 3


print ("The string representation of enum member is : ",end="") 
print (Plutus.employee) 

print ("The repr representation of enum member is : ",end="") 
print (repr(Plutus.employee)) 


print ("The type of enum member is : ",end ="") 
print (type(Plutus.employee)) 


print ("The name of enum member is : ",end ="") 
print (Plutus.employee.name) 
