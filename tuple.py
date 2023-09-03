users = ('Alex', 'John', 'Peter', 'Robert', 'Zack')
print(users)

for user in users:
    print(user)

user_list = [user + ' is the best' for user in users if len(user) <= 4]
print(user_list)