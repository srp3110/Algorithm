list = [{'id' : '#FF0000', 'color' : 'Red'},
        {'id' : '#800000', 'color' : 'Maroon'},
        {'id' : '#FFFF00', 'color' : 'Yellow'},
        {'id' : '#808000', 'color' : 'Olive'}]

new_list = []

for item in list:
    if item['id'] != '#FF0000':
        new_list.append(item)

print(new_list)