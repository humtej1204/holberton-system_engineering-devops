#!/usr/bin/python3
"""
    export data in the CSV format
"""

if __name__ == "__main__":
    import csv
    import json
    from sys import argv
    import requests

    # Data
    ID = argv[1]
    url_api = "https://jsonplaceholder.typicode.com"

    # Endpoints
    ep_user = "{}/users/{}".format(url_api, str(ID))
    ep_todos = "{}/todos".format(ep_user)

    # Requests
    user = requests.get(ep_user)
    todos = requests.get(ep_todos)

    # Format
    user = user.json()
    todos = todos.json()

    # Export to .csv file
    with open(ID + ".csv", "w", encoding="utf8") as file:
        writer = csv.writer(file, delimiter=",", quotechar="'")
        for task in todos:
            writer.writerow([
                json.dumps(ID),
                json.dumps(user.get("username")),
                json.dumps(str(task.get("completed"))),
                json.dumps(task.get("title"))
            ])
