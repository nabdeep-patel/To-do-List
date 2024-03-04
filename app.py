import streamlit as st

# Create a title for the app
st.title("To-Do List")

# Create a text input field for the user to enter a task
task = st.text_input("Enter a task")

# Create a button for the user to add the task to the list
add_task_button = st.button("Add Task")

# Create a list to store the tasks
tasks = []

# If the user clicks the add task button, add the task to the list
if add_task_button:
    tasks.append(task)

# Display the list of tasks
st.write("Tasks:")
for task in tasks:
    st.write(task)
