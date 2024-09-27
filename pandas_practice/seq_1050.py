import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='counts')
    return df[df['counts'] >= 3][['actor_id', 'director_id']]


if __name__ == '__main__':
    data = {
        'actor_id': [1, 1, 1, 1, 1, 2, 2],
        'director_id': [1, 1, 1, 2, 2, 1, 1],
        'timestamp': [0, 1, 2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)
    df = df.groupby(['actor_id', 'director_id']).size().reset_index(name='counts')
    print(df)
    # print(df[df['timestamp'] >= 3][['actor_id', 'director_id']])
