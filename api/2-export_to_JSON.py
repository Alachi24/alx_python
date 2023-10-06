# import json
# import requests
# import sys


# if len(sys.argv) != 2:
#     print("Usage: python3 2-export_to_JSON.py <employee_id>")
#     sys.exit(1)

# employee_id = sys.argv[1]
# url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
# response = requests.get(url)
# employee_name = response.json().get("username")

# if not employee_name:
#     print(f"No employee found with ID {employee_id}")
#     sys.exit(1)

# url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
# response = requests.get(url)
# todos = response.json()

# # Prepare the data in JSON format
# # Initialize as a list of dicts `employee_id` as the key and [] as the value

# employee_tasks = []
# for todo in todos:
#     task_data = {
#         "task": todo.get("title"),
#         "completed": todo.get("completed"),
#         "username": employee_name
#     }
#     employee_tasks.append(task_data)


# output_file = f"{employee_id}.json"

# with open(output_file, 'w') as json_file:
#     json.dump({employee_id: employee_tasks}, json_file, indent=4)

# print(f"Data exported to {output_file}")

import json
import requests
import sys


if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response = requests.get(url)
employee_name = response.json().get("username")

if not employee_name:
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
response = requests.get(url)
todos = response.json()

total_tasks = len(todos)
done_tasks = sum(1 for todo in todos if todo.get("completed"))

# Create a dictionary with the required format
result = {employee_id: [{"task": todo.get("title"), "completed": todo.get(
    "completed"), "username": employee_name} for todo in todos]}

# Export the data to a JSON file
with open(f"{employee_id}.json", "w") as json_file:
    json.dump(result, json_file, indent=4)

print(
    f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
for todo in todos:
    if todo.get("completed"):
        print(f"\t {todo.get('title')}")
