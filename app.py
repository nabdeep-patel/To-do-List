import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task, date):
    tasks.append({'Task': task, 'Date': date, 'Status': 'Pending'})

# Function to update task status
def update_status(task_index, new_status):
    tasks[task_index]['Status'] = new_status

# Function to display tasks
def display_tasks():
    st.subheader('To-Do List')
    tasks_df = pd.DataFrame(tasks)
    st.table(tasks_df)

# Main function
def main():
    st.title('To-Do List APK')

    # Input fields for task and date
    task = st.text_input('Task:')
    date = st.date_input('Due Date:', min_value=datetime.today())

    # Button to add task
    if st.button('Add Task'):
        add_task(task, date)

    # Display tasks
    display_tasks()

# Run the main function
if __name__ == '__main__':
    main()
