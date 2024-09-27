import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, department, left_on='departmentId', right_on='id').rename(
        columns={'id_x': 'id', 'name_x': 'Employee', 'salary': 'Salary', 'id_y': 'departmentId', 'name_y': 'Department'})
    max_salary = df.groupby('Department')['Salary'].transform('max')
    df = df[df['Salary'] == max_salary]
    return df[['Department', 'Employee', 'Salary']]


if __name__ == '__main__':
    employee = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
        'salary': [70000, 90000, 80000, 60000, 90000],
        'departmentId': [1, 1, 2, 2, 1]
    })

    department = pd.DataFrame({
        'id': [1, 2],
        'name': ['IT', 'Sales']
    })

