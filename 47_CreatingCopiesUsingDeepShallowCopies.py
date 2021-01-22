import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
old_list_deep = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_list = copy.copy(old_list)
new_list_deep = copy.deepcopy(old_list_deep)


old_list.append([4, 4, 4])
old_list[1][1] = 'AA'

old_list_deep[1][0] = 'BB'

new_list_deep = copy.deepcopy(old_list_deep)

print("Old list:", old_list)
print("New list:", new_list)
print("Old List before deep copying:", old_list_deep)
print("New list after using deep copy:", new_list_deep)
