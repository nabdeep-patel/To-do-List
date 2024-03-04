import streamlit as st
from datetime import datetime, timedelta

def add_task(tasks, task_name, due_date):
    tasks.append({"task_name": task_name, "due_date": due_date, "status": "Pending"})
    st.success("Task added successfully!")

def mark_as_completed(tasks, task_index):
    tasks[task_index]["status"] = "Completed"
    st.success("Task marked as completed!")

def check_missed_tasks(tasks):
    for task in tasks:
        due_date = datetime.strptime(task["due_date"], "%Y-%m-%d %H:%M:%S")
        if datetime.now() > due_date and task["status"] != "Completed":
            task["status"] = "Missed"
    return tasks

def main():
    st.title("Task Manager")

    tasks = st.session_state.get("tasks", [])

    if not tasks:
        st.session_state.tasks = []

    task_name = st.text_input("Enter task name:")
    due_date = st.date_input("Due date:")
    due_time = st.time_input("Due time:")

    if st.button("Add Task"):
        due_date_time = datetime.combine(due_date, due_time)
        add_task(tasks, task_name, due_date_time.strftime("%Y-%m-%d %H:%M:%S"))

    tasks = check_missed_tasks(tasks)

    if tasks:
        st.header("Tasks")
        for i, task in enumerate(tasks):
            st.write(f"**Task {i+1}:** {task['task_name']} - **Due Date:** {task['due_date']} - **Status:** {task['status']}")
            if task["status"] != "Completed":
                if st.button(f"Mark Task {i+1} as Completed"):
                    mark_as_completed(tasks, i)
    else:
        st.write("No tasks yet.")

if __name__ == "__main__":
    main()
