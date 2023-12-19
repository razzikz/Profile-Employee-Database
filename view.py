import json

with open('users.json') as file:
    data = json.load(file)

for user in data['users']:
    print(f'{user["name"]}    {user["salary"]}₽      {user["job_title"]}')

print("Hello, what are we doing?\n1 - delete\n2 - add\n3 - edit\n4 - exit")
choice, i = 0, 0
while i == 0:
    try:
        choice = int(input("Your choice: "))
        if choice in [1, 2, 3, 4]:
            from controller import *
            break
        else:
            print("Try once more")
    except ValueError:
        print("Try once more")