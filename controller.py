import json
from model import enter, Model, enter_name
from view import choice

with open('users.json') as file:
    data = json.load(file)

if choice == 1:
    enter = Model(enter_name(), 1, " ")
    enter.del_user(data)
elif choice == 2:
    enter.add_user(data)
elif choice == 3:
    enter.edit_user(data)

for user in data['users']:
    print(f'{user["name"]}    {user["salary"]}₽      {user["job_title"]}')

with open('users.json', 'w') as file:
    json.dump(data, file, indent=3)