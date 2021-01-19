class Student():  
    def __dir__(self):  
        return [0, 10, 20, 30]  
# Calling function  
s = Student()  
att = dir(s)  
# Displaying result  
print(att)  