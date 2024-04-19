# Dictionaries in Python

my_dict['new_key'] = 'new_value'

my_dict['existing_key'] = 'updated_value'

del my_dict['key_to_remove']

my_dict.pop('key_to_remove')

for key in my_dict:
    # do something with key

for key, value in my_dict.items():
    # do  something with key and value

keys = my_dict.keys()

values = my_dict.values()

items = my_dict.items()

value = my_dict.get('key')

my_dict.clear()

new_dict = my_dict.copy()

my_dict.update({'key3: 'value3'})
                
keys = ['a', 'b', 'c']
values = [1, 2 ,3]
my_dict = {key: value for key, value in zip(keys, values)}

if 'key' in my_dict:
    # do something