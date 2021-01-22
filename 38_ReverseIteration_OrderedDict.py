from collections import OrderedDict

Ordered_Dict1 = OrderedDict()

# adding elements to dict
Ordered_Dict1['Kangaroo'] = 7

# replacing a dict key value
Ordered_Dict1['Raspberry'] = 19
print(Ordered_Dict1)

# # removing and adding a value
# Ordered_Dict1.pop('Raspberry')
# print(Ordered_Dict1)
# Ordered_Dict1['kiwi'] = 4
# print(Ordered_Dict1)

for item in reversed(Ordered_Dict1):
    print(item)
    