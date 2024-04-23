from collections import defaultdict

my_dict_str= defaultdict(str)
my_dict_list= defaultdict(list)

print(my_dict_str['key']) # ''
print(my_dict_list['key']) # []

my_dict_str['key']+= 'Hello'
my_dict_list['key'].append(4)

print(my_dict_str['key']) # 'Hello'
print(my_dict_list['key']) # [4]