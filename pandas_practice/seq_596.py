import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class').count().reset_index()
    print(df)
    return df[df['student'] >= 5][['class']]


if __name__ == '__main__':
    data = {
        'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']
    }

    df = pd.DataFrame(data)
    print(find_classes(df))
