import numpy as np
import pandas as pd
import requests


def extract_counts(df):

    df_ts = df[['date', 'id']]
    new_dates = pd.Series([x[:10]
                           for x in df['date'].values], name='new_dates')
    new_dates_s = new_dates.str.split('-', expand=True)
    new_dates_s = new_dates_s.rename(columns={0: 'year', 1: 'month', 2: 'day'})

    df_ts = pd.concat([df_ts, new_dates_s], axis=1)
    df_ts = df_ts.loc[:, "id":"day"].rename(columns={'id': 'count'})
    df_ts = df_ts.groupby(['year', 'month', 'day']).count()

    # print(df_ts)
    covid1 = pd.Series(df_ts['count'].values, name='count')
    covid2 = pd.Series(new_dates.unique(), name="date").sort_values()
    covid = pd.concat([covid2.reset_index(), covid1], axis=1)
    covid["date"] = pd.to_datetime(covid['date'])
    covid = covid.set_index('date').drop('index', axis=1)
    return covid


def get_data_from_HS():
    data = requests.get(
        "https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaData")
    data_json = data.json()
    return data_json
