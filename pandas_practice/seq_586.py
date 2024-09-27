import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby('customer_number').count().reset_index().sort_values('order_number', ascending=False)
    return df[['customer_number']][0:1]


if __name__ == '__main__':
    data = {
        'order_number': [1, 2, 3, 4],
        'customer_number': [1, 2, 3, 3]
    }
    df = pd.DataFrame(data)
    df = df.groupby('customer_number').count().reset_index().sort_values('order_number', ascending=False)
    print(type(df['customer_number']))
    print(type(df[['customer_number']]))
