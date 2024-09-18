import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee[['salary']].drop_duplicates().sort_values('salary', ascending=False)
    if len(employee) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    return employee.head(2).tail(1).rename(columns={'salary': 'SecondHighestSalary '})
