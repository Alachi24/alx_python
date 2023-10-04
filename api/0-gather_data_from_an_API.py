import requests


def get_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)

    if response.status_code == 200:
        employee_data = response.json()
        employee_name = employee_data["name"]
    else:
        print(f"Employee with ID {employee_id} not found.")
        return

    # Fetch employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)

    if response.status_code == 200:
        todo_list = response.json()
    else:
        print(f"TODO list for employee {employee_name} not found.")
        return

    # Calculate progress
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task["completed"])

    # Display progress
    print(
        f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

    for task in todo_list:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
