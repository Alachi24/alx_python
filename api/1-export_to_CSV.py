import csv
import requests
import sys


def export_employee_data(employee_id):
    # Fetch employee details
    try:
        response_user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}')
        response_user.raise_for_status()
        user_data = response_user.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return

    # Fetch employee's tasks
    try:
        response_todos = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
        response_todos.raise_for_status()
        todos_data = response_todos.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return

    # Prepare CSV file name based on the employee's ID
    csv_filename = f'{employee_id}.csv'

    # Write tasks to CSV
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write CSV header
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write tasks
        for task in todos_data:
            csv_writer.writerow(
                [employee_id, user_data["username"], str(task["completed"]), task["title"]])

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py employee_id1 employee_id2 ...")
        sys.exit(1)

    employee_ids = sys.argv[1:]
    for emp_id in employee_ids:
        export_employee_data(int(emp_id))
