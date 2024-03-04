import streamlit as st
import pandas as pd
from datetime import datetime

# Create empty DataFrame to store tasks
tasks_df = pd.DataFrame(columns=['Task', 'Date', 'Status'])

# Function to add a task
def add_task(task, date):
    global tasks_df
    tasks_df = tasks_df.append({'Task': task, 'Date': date, 'Status': 'Pending'}, ignore_index=True)

# Function to update task status
def update_status(task, new_status):
    global tasks_df
    tasks_df.loc[tasks_df['Task'] == task, 'Status'] = new_status

# Function to display tasks
def display_tasks():
    st.subheader('To-Do List')
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
