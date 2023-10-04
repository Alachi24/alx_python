import csv
import requests
import sys


if len(sys.argv) != 2:
    print("Usage: python3 1-export_to_CSV.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response = requests.get(url)
employee_name = response.json().get("name")

if not employee_name:
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
response = requests.get(url)
todos = response.json()

filename = f"{employee_id}.csv"
with open(filename, mode='w', newline='') as csv_file:
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for todo in todos:
        writer.writerow({'USER_ID': employee_id,
                         'USERNAME': employee_name,
                         'TASK_COMPLETED_STATUS': str(todo.get('completed')),
                         'TASK_TITLE': todo.get('title')})
print(f"Data exported to {filename}")
