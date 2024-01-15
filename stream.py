import requests
import streamlit as st

# Define the FastAPI endpoint URL
FASTAPI_URL = "http://127.0.0.1:8000"  # Update with your FastAPI server URL

# Streamlit UI elements
st.title('Todo App')

# Function to get all todos from FastAPI
def get_todos():
    response = requests.get(f"{FASTAPI_URL}/todos/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching todos. Status code: {response.status_code}")

# Function to create a new todo using FastAPI
def create_todo(title):
    payload = {"title": title, "completed": False}
    response = requests.post(f"{FASTAPI_URL}/todos/", json=payload)
    if response.status_code == 200:
        st.success("Todo created successfully!")
    else:
        st.error(f"Error creating todo. Status code: {response.status_code}")

# Get all todos and display them
todos = get_todos()
if todos:
    st.write("### Todos:")
    for todo in todos:
        st.write(f"- {todo['title']}")

# Create new todo form
st.write("### Create a New Todo:")
new_todo_title = st.text_input("Enter Todo Title:")
if st.button("Create Todo"):
    if new_todo_title:
        create_todo(new_todo_title)
    else:
        st.warning("Please enter a title for the todo.")
