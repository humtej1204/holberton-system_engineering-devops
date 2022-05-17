#!/usr/bin/python3
"""
    Dictionary of list of dictionaries,
    export data in the JSON format
"""
if __name__ == "__main__":
    import json
    import requests

    # Data
    url_api = "https://jsonplaceholder.typicode.com"

    # Endpoints
    ep_users = "{}/users".format(url_api)

    # Requests
    users = requests.get(ep_users)

    # Format
    users = users.json()

    # Output
    json_to_export = {}
    with open("todo_all_employees.json", "w", encoding="utf8") as file:
        for user in users:
            json_to_export[user.get("id")] = []
            ep_user_todos = "{}/{}/todos".format(ep_users, user.get("id"))
            todos = requests.get(ep_user_todos).json()
            for task in todos:
                json_to_export[user.get("id")].append({
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
        json.dump(json_to_export, file)
