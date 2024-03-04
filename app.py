
import streamlit as st
from datetime import datetime

# Function to classify the task based on time
def classify_task(task_time):
    now = datetime.now()
    if now > task_time:
        return "Missed"
    elif now == task_time:
        return "Due"
    else:
        return "Pending"

# Function to display tasks
def display_tasks(tasks):
    st.write("### Tasks")
    if not tasks:
        st.write("No tasks added yet.")
    else:
        for task in tasks:
            status = classify_task(task['time'])
            st.write(f"- **{task['name']}**: {status}")

# Function to add a new task
def add_task(tasks, name, time):
    tasks.append({'name': name, 'time': time})

def main():
    st.title("Task Manager")

    tasks = []

    task_name = st.text_input("Task Name")
    task_time = st.date_input("Task Date")  # Can be modified to include time as well

    if st.button("Add Task"):
        add_task(tasks, task_name, task_time)

    display_tasks(tasks)

if __name__ == "__main__":
    main()
