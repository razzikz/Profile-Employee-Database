def del_user(data):
    name = enter_name()
    data["users"] = [user for user in data["users"] if user["name"] != name]


def add_user(data):
    name = enter_name()
    salary = enter_salary()
    job_title = enter_job()
    data['users'].append({
        "name": name,
        "salary": salary,
        "job_title": job_title
    })


def edit_user(data):
    name = enter_name()
    salary = enter_salary()
    job_title = enter_job()
    data["users"] = [user for user in data["users"] if user["name"] != name]
    data['users'].append({
        "name": name,
        "salary": salary,
        "job_title": job_title
    })


def enter_name():
    try:
        name = input("Name users: ")
        return name
    except ValueError:
        print('Try once more')


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


def enter_job():
    while True:
        job_title = input("Job title users: ")
        if job_title:
            return job_title
        else:
            print("Try once more")