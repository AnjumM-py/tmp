import pandas as pd

# Creating the DataFrame
data = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}

students = pd.DataFrame(data)

# Finding the index of the student_id = 101
index = students.index[students['student_id'] == 101].tolist()[0]

# Using .iloc to select the name and age
result = students.iloc[[index], [1, 2]]  # Column index 1 is 'name', 2 is 'age'

# Display the result
print(result)
