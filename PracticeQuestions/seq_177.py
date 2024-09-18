import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee[['salary']].drop_duplicates('salary').sort_values('salary', ascending=False)
    if N > len(employee) or N <= 0:
        return pd.DataFrame({'getNthHighestSalary(' + str(N) + ')': [None]})
    return employee.head(N).tail(1).rename(columns={'salary': 'getNthHighestSalary(' + str(N) + ')'})


if __name__ == '__main__':
    data = {
        'id': [1, 2, 3],
        'salary': [100, 200, 300]
    }
    df = pd.DataFrame(data)
    print(nth_highest_salary(df, 2))
