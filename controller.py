from model import *
import json
from view import choice

with open('users.json') as file:
    data = json.load(file)

if choice == 1:
    del_user(data)
    for user in data['users']:
        print(f'{user["name"]}    {user["salary"]}₽      {user["job_title"]}')

elif choice == 2:
    add_user(data)
    for user in data['users']:
        print(f'{user["name"]}    {user["salary"]}₽      {user["job_title"]}')

elif choice == 3:
    edit_user(data)
    for user in data['users']:
        print(f'{user["name"]}    {user["salary"]}₽      {user["job_title"]}')

elif choice == 4:
    print("GoodBye!")


with open('users.json', 'w') as file:
    json.dump(data, file, indent=3)