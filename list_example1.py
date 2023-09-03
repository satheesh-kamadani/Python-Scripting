users = ['Alex', 'Viktor', 'David', 'Thomes', 'Zack']

for user in users[:3]:
    print(f"The current user is {user}")

new_list = [item + ' is the best' for item in users if len(item)>4]
print(new_list)

new_list = [item + ' is the best' for item in users if len(item)>4]
print(new_list)

if not len(users) > 6:
    print('It is longer then 2 items')
else:
    print('It is not longer then 2 items')

if 'satheesh' in users:
    print('It is in the list')
else:
    print('It is not in the list')

if len(users) > 4 and 'Alex' in users:
    print('It is in the list')
else:
    print('It is not there in the list')


