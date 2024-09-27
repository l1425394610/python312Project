import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby(['teacher_id'])['subject_id'].nunique().reset_index().rename(columns={'subject_id': 'cnt'})


if __name__ == '__main__':
    data = pd.DataFrame({
        'teacher_id': [1, 1, 1, 2, 2, 2, 2],
        'subject_id': [2, 2, 3, 1, 2, 3, 4],
        'dept_id': [3, 4, 3, 1, 1, 1, 1]
    })

    df = pd.DataFrame(data=data)
    df = df.groupby(['teacher_id'])['subject_id'].nunique().reset_index()
    print(df)
