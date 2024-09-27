import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    employees.loc[(employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M')), 'bonus'] = employees[
        'salary']
    return employees[['employee_id', 'bonus']].sort_values('employee_id')


if __name__ == '__main__':
    data = {
        'employee_id': [2, 3, 7, 8, 9],
        'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
        'salary': [3000, 3800, 7400, 6100, 7700],
    }
    df = pd.DataFrame(data)
    print(calculate_special_bonus(df))
