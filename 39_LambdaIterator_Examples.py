# Degree celsius to fahrenheit

C = [32, 31, 108, 0, 44] 
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)

# Using map and lambda operator to solve arithmetic equation

a = [1, 2, 3]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
 
result = list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))
print(result)

