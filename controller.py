from model import *
import json

with open('users.json') as file:
    data = json.load(file)

if choice == 1:
    del_user(data)
    print(data)

elif choice == 2:
    add_user(data)
    print(data)

elif choice == 3:
    edit_user(data)
    print(data)

elif choice == 4:
    print("GoodBye!")


with open('users.json', 'w') as file:
    json.dump(data, file)