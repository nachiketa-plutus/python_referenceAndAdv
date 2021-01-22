# This is a simple generator for Fibonacci Numbers 
def fibonacci(): 
	
	# Initializinf first two Fibonacci Numbers 
	a, b = 0, 1

	# One by one yield next Fibonacci Number 
	while True: #a < limit: 
		yield a 
		a, b = b, a + b 

# Create a generator object 
f = fibonacci() 


counter = 0 
for x in f:
    print(x),
    counter = counter+1
    if(counter>10):
        break
print

# Iterating over the generator object using next 
# print x.next() # In Python 3, __next__() 
# print x.next() 
# print x.next() 
# print x.next() 
# print x.next()

# Iterating over the generator object using for 
# in loop. 
# print("\nUsing for in loop") 
# for i in fib(5): 
# 	print(i) 
