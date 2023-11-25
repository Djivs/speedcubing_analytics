import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def h1(results_df):
    ok_results = results_df[results_df['average'] != -1]
    old_results = ok_results[ok_results['year'] <= 2011].count().sum()
    new_results = ok_results[ok_results['year'] > 2011].count().sum()

    old_and_new = pd.DataFrame(
        {
            'year': ['до 2011', 'после 2011'],
            'count': [old_results, new_results]
        }
    )
    old_and_new.set_index('year', inplace=True)
    return old_and_new.plot(kind='pie', figsize=(6, 6), subplots=True)


def h2(results_df):
    results_df = results_df.drop(results_df[results_df.eventName == '3x3x3 Blind Old Style'].index)
    results_df = results_df.drop(results_df[results_df.eventName == '3x3x3 Multi-Blind Old Style'].index)
    results_df = results_df['eventName'].value_counts()

    return results_df.plot(kind='bar', figsize=(7, 7))


def h3(competitions_df):
    usa_comp_amount = competitions_df[competitions_df.countryName == 'United States'].count().sum()
    europe_comp_amount = competitions_df[competitions_df.continentId == '_Europe'].count().sum()
    usa_europe_df = pd.DataFrame(
        {'country': ['Европа', 'США'], 'Количество соревнований': [europe_comp_amount, usa_comp_amount]})
    usa_europe_df.set_index('country', inplace=True)
    return usa_europe_df.plot(kind='pie', subplots=True)


def h4(results_df):
    df_4 = results_df.drop(results_df[results_df.year < 2004].index)
    df_4 = df_4[df_4['eventName'] == '3x3x3 Cube'].groupby('year')['average'].mean()
    plt.xticks(np.arange(2004, 2016, 1))
    return df_4.plot()


def h5(results_df):
    df_5 = results_df.drop(results_df[results_df.eventName == '3x3x3 Blind Old Style'].index)
    df_5 = df_5.drop(df_5[df_5.eventName == '3x3x3 Multi-Blind Old Style'].index)
    df_5 = df_5[df_5['average'] == -1].groupby('eventName')['average'].count().sort_values()
    return df_5.plot(kind='pie', figsize=(7, 7))
