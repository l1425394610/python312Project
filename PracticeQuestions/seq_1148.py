import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]['viewer_id']
    return pd.DataFrame({'id': df.drop_duplicates().sort_values()})


if __name__ == '__main__':
    data = {
        'article_id': [1, 1, 2, 2, 4, 3, 3],
        'author_id': [3, 3, 7, 7, 7, 4, 4],
        'viewer_id': [5, 6, 7, 6, 1, 4, 4],
        'view_date': ['2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02', '2019-07-22', '2019-07-21', '2019-07-21']
    }
    # print(pd.DataFrame(data))
    print(article_views(pd.DataFrame(data)))
