import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    return users.sort_values(by='user_id', ascending=True)


if __name__ == '__main__':
    data = {
        'user_id': [1, 2],
        'name': ['alice', 'bOB']
    }
    df = pd.DataFrame(data)
    fix_names(df)
    print(df)
