import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets['content'].str.len() >= 1]
    print(df)
    return pd.DataFrame({'tweet_id':df['tweet_id']})
