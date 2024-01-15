import requests

BASE_URL = "http://127.0.0.1:8000"

# Function to get JWT token
def login(username, password):
    response = requests.post(f"{BASE_URL}/login/", data={"username": username, "password": password})
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("Invalid username or password")
        return None

# Function to create a new Todo
def create_todo(title, description, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/todos/", json={"title": title, "description": description}, headers=headers)
    if response.status_code == 200:
        print("Todo added successfully")
    else:
        print("Failed to add todo")

# Function to delete a Todo
def delete_todo(todo_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}", headers=headers)
    if response.status_code == 200:
        print("Todo deleted successfully")
    else:
        print("Failed to delete todo")

if __name__ == "__main__":
    username = input("Username: ")
    password = input("Password: ")
    
    token = login(username, password)
    if token:
        while True:
            print("\nMenu:")
            print("1. Create Todo")
            print("2. Delete Todo")
            print("3. Exit")

            choice = input("Enter choice (1/2/3): ")

            if choice == "1":
                title = input("Enter Todo Title: ")
                description = input("Enter Todo Description: ")
                create_todo(title, description, token)
            elif choice == "2":
                todo_id = input("Enter Todo ID to delete: ")
                delete_todo(todo_id, token)
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
