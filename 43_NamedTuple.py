# Aim: To demonstrate the utility of namwdtuple(), _make(), _asdict()

import collections 

Student = collections.namedtuple('Student',['name','age','DOB']) 

S = Student('Nandini','19','2541997') 

li = ['Manjeet', '19', '411997' ] # This is to initialize iterables 

di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' } 
 
print ("Instance of namedtuple using iterable is : ") 

# _make(): This function returns the namedtuple from the iterable passed as argument
print (Student._make(li))

# _asdict(): To return an OrderedDict()
print ("The OrderedDict instance using namedtuple is : ") 
print (S._asdict()) 

# using ** operator to return namedtuple from dictionary 
print ("The namedtuple instance from dict is : ") 

# To convert a dictionary into a namedtuple using ** operator. 
print (Student(**di)) 
