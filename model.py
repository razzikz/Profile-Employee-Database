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


class Model:
    def __init__(self, name, salary, job):
        self.name = name
        self.salary = salary
        self.job = job

    def del_user(self, data):
        data["users"] = [user for user in data["users"] if user["name"] != self.name]

    def add_user(self, data):
        data['users'].append({
            "name": self.name,
            "salary": self.salary,
            "job_title": self.job
        })

    def edit_user(self, data):
        data["users"] = [user for user in data["users"] if user["name"] != self.name]
        data['users'].append({
            "name": self.name,
            "salary": self.salary,
            "job_title": self.job
        })


enter = Model(enter_name(), enter_salary(), enter_job())