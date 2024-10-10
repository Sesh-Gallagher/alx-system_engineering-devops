#!/usr/bin/python3
"""python script that assist in accessing\
REST API for todo lists of employees"""

import requests
import re
import sys


if __name__ == '__main__':
    REST_API = "https://jsonplaceholder.typicode.com/"
    user = requests.get(REST_API + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(REST_API + "todos",
    params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
    user.get("name"), len(completed), len(todos)))
	[print("\t {}".format(c)) for c in completed]
