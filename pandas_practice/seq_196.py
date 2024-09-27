import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # person = person.sort_values('id')
    # person.drop_duplicates(subset='email', keep='first', inplace=True)
    # return

    min_id = person.groupby('email')['id'].transform('min')
    print(min_id)
    removed_person = person[person['id'] != min_id]
    person.drop(removed_person.index, inplace=True)


if __name__ == '__main__':
    data = {
        'id': [1, 2, 3],
        'email': ['john@example.com', 'bob@example.com', 'john@example.com']
    }
    df = pd.DataFrame(data)
    delete_duplicate_emails(df)
