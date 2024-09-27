import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    groups = activities.groupby('sell_date')
    stats = groups.agg(
        num_sold=('product', 'nunique'),
        products=('product', lambda x: ','.join(sorted((set(x)))))
    ).reset_index()
    stats.sort_values('sell_date', inplace=True)
    return stats


if __name__ == '__main__':
    data = {
        'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30'],
        'product': ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-Shirt']
    }
    df = pd.DataFrame(data)
    df = df.groupby('sell_date').agg(num_sold=('product', 'nunique'),
                                     products=('product', lambda x: ','.join((set(x)))))
    df = df.reset_index()
    print(df)
