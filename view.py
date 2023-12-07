print("Hello, what are we doing?\n1 - delete\n2 - add\n3 - edit\n4 - exit")

while True:
    try:
        choice = int(input("Your choice: "))
        while True:
            if 1 < choice > 4:
                print("Try once more")
                choice = int(input("Your choice: "))
            else:
                break
        break
    except ValueError:
        print("Try once more")


def enter_name():
    while True:
        name = input("Name users: ")
        if name:
            return name
        else:
            print("Try once more")


def enter_job():
    while True:
        job_title = input("Job title users: ")
        if job_title:
            return job_title
        else:
            print("Try once more")


def enter_salary():
    while True:
        try:
            salary = int(input("Salary users (in ₽): "))
            if salary > 0:
                return salary
            else:
                print("Try once more. Salary not must be 0")
        except ValueError:
            print("Try once more")