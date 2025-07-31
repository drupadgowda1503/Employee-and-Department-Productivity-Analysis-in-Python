#To

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('C:\\Users\\Lenovo\\Documents\\EDA project\\EDA_project001.csv')#use ur file path here
df = pd.DataFrame(data)

# Convert the DATE column to datetime
df['DATE'] = pd.to_datetime(df['DATE'])

# Clean the data
df['PROJECT_NAME'] = df['PROJECT_NAME'].str.strip().str.lower()

# Analyze employee performance based on tasks completed and average hours worked
employee_performance = df.groupby('EMPLOYEE_ID').agg({
    'HOURS_WORKED': 'mean',
    'TASKS_COMPLETED': 'sum'
}).reset_index()

# Rename columns for clarity
employee_performance.rename(columns={
    'HOURS_WORKED': 'AVERAGE_HOURS_WORKED',
    'TASKS_COMPLETED': 'TOTAL_TASKS_COMPLETED'
}, inplace=True)

# Group employees by departments and compare productivity
department_performance = df.groupby('DEPARTMENT').agg({
    'HOURS_WORKED': 'mean',
    'TASKS_COMPLETED': 'mean'
}).reset_index()

# Visualize the correlation between working hours and task completion rates
plt.figure(figsize=(10, 6))
sns.scatterplot(data=employee_performance, x='AVERAGE_HOURS_WORKED', y='TOTAL_TASKS_COMPLETED')
plt.title('Correlation between Average Hours Worked and Total Tasks Completed')
plt.xlabel('Average Hours Worked')
plt.ylabel('Total Tasks Completed')
plt.grid(True)
plt.show()

# Bar plot for department productivity comparison
plt.figure(figsize=(12, 8))
sns.barplot(data=department_performance, x='DEPARTMENT', y='HOURS_WORKED', color='skyblue', label='Average Hours Worked')
sns.barplot(data=department_performance, x='DEPARTMENT', y='TASKS_COMPLETED', color='orange', label='Average Tasks Completed', alpha=0.7)
plt.title('Department Productivity Comparison')
plt.xlabel('Department')
plt.ylabel('Average Metrics')
plt.legend()
plt.show()