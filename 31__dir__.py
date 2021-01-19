class Student():  
    def __dir__(self): 
      return [0, 10, 20, 30]      
# Calling function  
s = Student()  
attri = dir(s)  
# To display the result  
print(attri)  