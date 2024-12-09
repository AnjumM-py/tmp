import pandas as pd

# Creating the DataFrame
data = {
    'employee_id': [3, 90, 9, 60, 49, 43],
    'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    'salary': [48675, 11096, 33805, 37678, 23793, 40454]
}

employees = pd.DataFrame(data)

# Displaying the first and last rows
result = pd.concat([employees.iloc[[0]], employees.iloc[[-1]]])

# Display the result
print(result)
