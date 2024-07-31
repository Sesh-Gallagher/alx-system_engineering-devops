#!/usr/bin/python3
"""python script that assist in accessing\
	 REST API for todo lists of employees"""

import sys
import requests


if __name__ == '__main__':
    employeeId = sys.argv[1]
    REST_API = "https://jsonplaceholder.typicode.com/users"
    url = REST_API + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
