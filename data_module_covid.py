import numpy as np
import pandas as pd
import requests
import functools


def extract_counts(df):

    new_dates = pd.Series([x[:10]
                           for x in df['date'].values], name='new_dates')
    new_dates = pd.to_datetime(new_dates)

    res = pd.concat([new_dates, pd.Series(
        np.ones(len(new_dates)), name="count")], axis=1)

    res = res.groupby('new_dates').count()

    res['days_from_beginning'] = (res.index - res.index[0])
    res['days_from_beginning'] = res['days_from_beginning'].dt.days.astype(int)
    res['cum_sum'] = res['count'].cumsum()
    return res.reset_index()


def get_data_from_HS():
    data = requests.get(
        "https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaData")
    data_json = data.json()
    return data_json
