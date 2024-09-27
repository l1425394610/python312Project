import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score', 'rank']].sort_values(by='rank', ascending=True)


if __name__ == '__main__':
    data = {
        'id': [1, 2, 3, 4, 5, 6],
        'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
    }
    df = pd.DataFrame(data)
    df['rank'] = df['score'].rank(method='dense', ascending=False)
    print(df[['score', 'rank']].sort_values(by='rank', ascending=True))
