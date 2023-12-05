print("Hello, what are we doing? (1 - delete, 2 - add, 3 - exit)")
while True:
    try:
        choice = int(input("Your choice: "))
        name = input("Name new users: ")
        salary = int(input("Salary new users: "))
        job_title = input("Job title new users: ")
    except ValueError:
        print("Try once more")
    if choice == 3:
        break