import json

with open('users.json') as file:
    data = json.load(file)

for user in data['users']:
    print(f'{user["name"]}\n{user["salary"]}₽\n{user["job_title"]}')

print("Hello, what are we doing?\n1 - delete\n2 - add\n3 - edit\n4 - exit")
i = 0
while i == 0:
    try:
        choice = int(input("Your choice: "))
        while True:
            if 1 < choice > 4:
                print("Try once more")
                choice = int(input("Your choice: "))
            else:
                i = 1
                break
            break
    except ValueError:
        print("Try once more")

    from controller import *