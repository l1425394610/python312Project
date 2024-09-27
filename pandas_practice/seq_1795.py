import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = products.melt(id_vars='product_id', value_vars=['store1', 'store2', 'store3'], var_name='store', value_name='price')
    return products[products.notna()]


if __name__ == '__main__':
    data = {
        'product_id': [0, 1],
        'store1': [95, 70],
        'store2': [100, None],
        'store3': [105, 80]
    }
    df = pd.DataFrame(data)
    df = df.melt(id_vars='product_id', value_vars=['store1', 'store2', 'store3'], var_name='store', value_name='price')
    df = df.loc[df['price'].notna()]
    print(df)
