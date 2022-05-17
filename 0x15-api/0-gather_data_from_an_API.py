#!/usr/bin/python3
"""
    script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    # Data
    ID = argv[1]
    url_api = "https://jsonplaceholder.typicode.com"

    # Endpoints
    ep_user = "{}/users/{}".format(url_api, str(ID))
    ep_todos = "{}/todos".format(ep_user)
    ep_todos_completed = "{}?completed=true".format(ep_todos)

    # Requests
    user = requests.get(ep_user)
    todos = requests.get(ep_todos)
    todos_completed = requests.get(ep_todos_completed)

    # Format
    user = user.json()
    todos = todos.json()
    completed = todos_completed.json()

    # Output
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)
    ))
    for task in completed:
        print("\t {}".format(task.get("title")))
