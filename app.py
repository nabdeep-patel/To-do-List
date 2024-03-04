import streamlit as st

# Create a title for the app
st.title("To-Do List")

# Create a text input field for the user to enter a task
task = st.text_input("Enter a task")

# Create a button for the user to add the task to the list
add_task_button = st.button("Add Task")

# Create a list to store the tasks
tasks = []

# Create a button to insert time and date
insert_time_date_button = st.button("Insert Time and Date")

# If the user clicks the add task button, add the task to the list
if add_task_button:
    tasks.append({"task": task, "status": "Pending"})

# If the user clicks the insert time and date button, insert the time and date
if insert_time_date_button:
    time = st.time_input("Time:")
    date = st.date_input("Date:")
    tasks.append({"task": task, "time": time, "date": date, "status": "Pending"})

# Display the list of tasks
st.write("Tasks:")
table_columns = ["Date", "Time", "Task", "Status"]
task_rows = []
for task in tasks:
    task_row = [
        task.get("date", ""),
        task.get("time", ""),
        task.get("task", ""),
        task.get("status", ""),
    ]
    task_rows.append(task_row)

st.table(task_rows, columns=table_columns)
