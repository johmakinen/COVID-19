import numpy as np
import pandas as pd
import requests


def extract_counts(df):

    new_dates = pd.Series([x[:10]
                           for x in df['date'].values], name='new_dates')
    new_dates = pd.to_datetime(new_dates)

    res = pd.concat([new_dates, pd.Series(
        np.ones(len(new_dates)), name="count")], axis=1)

    return res.groupby('new_dates').count()


def get_data_from_HS():
    data = requests.get(
        "https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaData")
    data_json = data.json()
    return data_json
