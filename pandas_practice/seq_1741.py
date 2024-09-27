import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    df = employees.groupby(['emp_id', 'event_day'])['total_time'].sum().reset_index()
    df= df.rename(columns={'event_day': 'day'})
    return df


if __name__ == '__main__':
    data = {
        'emp_id': [1, 1, 1, 2, 2],
        'event_day': ['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-14-09'],
        'in_time': [4, 55, 1, 3, 47],
        'out_time': [32, 200, 42, 33, 74]
    }

    df = pd.DataFrame(data)
    df = total_time(df)
    print(df)
