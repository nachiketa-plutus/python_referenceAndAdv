from collections import OrderedDict

# creating a regular dictionary
dict_Nachiketa = {'banana': 6, 'kiwi': 8, 'koala': 22}

# creating an empty ordered dictionary
ordered_dict = OrderedDict()
print(ordered_dict)

# creating ordered dict from dictionary created earliet
ordered_dict = OrderedDict(dict_Nachiketa)
print(ordered_dict)