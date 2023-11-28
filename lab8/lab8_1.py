
import requests

# Task 1.1
post_id = 1
url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'
response = requests.get(url)

print("Task 1.1:")
if response.status_code >= 400:
    print(f"error! Status Code: {response.status_code}")
else:
    print("Response Content:")
    print(response.json())

# Task 1.2 and 1.3
class ToDo:
    def __init__(self, user_id, title, completed):
        self.user_id = user_id
        self.title = title
        self.completed = completed

new_todo = ToDo(user_id=1, title="Sample Todo", completed=False)

# Task 1.4
new_todo_dict = {
    "userId": new_todo.user_id,
    "title": new_todo.title,
    "completed": new_todo.completed
}

post_response = requests.post('https://jsonplaceholder.typicode.com/todos', json=new_todo_dict)

print("\nTask 1.4:")
if post_response.status_code >= 400:
    print(f"Error! Status Code: {post_response.status_code}")
else:
    print("Post Response Content:", post_response.json())
   

# Task 1,5
new_todo.completed = True

# Task 1.6: PUT Request
put_url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'
put_response = requests.put(put_url, json=new_todo_dict)

print("\nTask 1.6:")
if put_response.status_code >= 400 :
    print(f"Error! Status Code: {put_response.status_code}")
else:
    print("Put Response Content:", put_response.json())

