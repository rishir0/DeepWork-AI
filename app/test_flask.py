import requests

base_url = "http://127.0.0.1:5000"

def test_home():
    response = requests.get(base_url)
    print("GET /")
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

def test_add_task(task, priority):
    data = {'task': task, 'priority': priority}
    response = requests.post(f"{base_url}/add", data=data)
    print("POST /add")
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

def test_clear_tasks():
    response = requests.post(f"{base_url}/clear")
    print("POST /clear")
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

if __name__ == "__main__":
    test_home()
    test_add_task("Test Task", 2)
    test_home()  # Check if the task was added
    test_clear_tasks()
    test_home()  # Check if the tasks were cleared
