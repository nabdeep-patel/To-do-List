import streamlit as st
import pandas as pd

# Function to load existing tasks from file or create a new one if it doesn't exist
def load_tasks():
    try:
        tasks = pd.read_csv("tasks.csv")
    except FileNotFoundError:
        tasks = pd.DataFrame(columns=["Task", "Due Date", "Status"])
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    tasks.to_csv("tasks.csv", index=False)

# Main function to run the app
def main():
    st.title("To-Do List App")

    tasks = load_tasks()

    # Sidebar to add new tasks
    st.sidebar.header("Add New Task")
    new_task = st.sidebar.text_input("Task:")
    due_date = st.sidebar.date_input("Due Date:")
    if st.sidebar.button("Add Task"):
        tasks = tasks.append({"Task": new_task, "Due Date": due_date, "Status": "Pending"}, ignore_index=True)
        save_tasks(tasks)

    # Show tasks table
    st.header("Your Tasks")
    st.dataframe(tasks)

    # Show tasks status
    st.header("Tasks Status")
    status_counts = tasks["Status"].value_counts()
    st.write(f"Completed: {status_counts.get('Completed', 0)}")
    st.write(f"Missed: {status_counts.get('Missed', 0)}")
    st.write(f"Pending: {status_counts.get('Pending', 0)}")

if __name__ == "__main__":
    main()
