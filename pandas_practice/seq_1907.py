import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = (accounts['income'] < 20000).sum()
    high_salary = (accounts['income'] > 50000).sum()
    average_salary = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_salary, average_salary, high_salary]
    })
