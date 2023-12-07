from view import *


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