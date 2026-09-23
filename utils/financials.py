import pandas as pd


def safe_get(df, keys):
    for key in keys:
        if key in df.columns:
            return df[key].fillna(0)

    return pd.Series(0, index=df.index)
