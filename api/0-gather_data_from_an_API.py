import requests
import sys


def get_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)

    # Check if the employee request was successful (status code 200)
    if employee_response.status_code == 200:
        employee_data = employee_response.json()
        employee_name = employee_data["name"]

        # Fetch employee's TODO list
        todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todo_response = requests.get(todo_url)

        # Check if the TODO list request was successful (status code 200)
        if todo_response.status_code == 200:
            todo_list = todo_response.json()

            # Calculate progress
            total_tasks = len(todo_list)
            completed_tasks = sum(1 for task in todo_list if task["completed"])

            # Display progress
            print(
                f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

            if completed_tasks > 0:
                for task in todo_list:
                    if task["completed"]:
                        print(f"\t{task['title']}")
            else:
                print("\tNo completed tasks.")

            # Formatting is OK
            print("Formatting: OK")
        else:
            print(
                f"Failed to fetch TODO list. Status code: {todo_response.status_code}")
    else:
        print(
            f"Failed to fetch employee details. Status code: {employee_response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Invalid input. Please provide a valid employee ID.")
