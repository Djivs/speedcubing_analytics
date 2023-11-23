import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    # load data
    results_df = pd.read_csv('WCA_export_Results.tsv', sep='\t')
    competitions_df = pd.read_csv('WCA_export_Competitions.tsv', sep='\t')
    events_df = pd.read_csv('WCA_export_Events.tsv', sep='\t')
    round_types_df = pd.read_csv('WCA_export_RoundTypes.tsv', sep='\t')
    persons_df = pd.read_csv('WCA_export_Persons.tsv', sep='\t')
    formats_df = pd.read_csv('WCA_export_Formats.tsv', sep='\t')
    countries_df = pd.read_csv('WCA_export_Countries.tsv', sep='\t')

    # merge data
    persons_df = pd.merge(persons_df, countries_df, on='countryId', how='inner')
    competitions_df = pd.merge(competitions_df, countries_df, on='countryId', how='inner')

    results_df = pd.merge(results_df, competitions_df, on='competitionId', how='inner')
    results_df = pd.merge(results_df, events_df, on='eventId', how='inner')
    results_df = pd.merge(results_df, round_types_df, on='roundTypeId', how='inner')
    results_df = pd.merge(results_df, persons_df, on='personId', how='inner')
    results_df = pd.merge(results_df, formats_df, on='formatId', how='inner')

    # clean data
    results_df.drop_duplicates(
        subset=['competitionId', 'personId', 'roundTypeId', 'eventId', 'value1', 'value2', 'value3',
                'value4', 'value5'])

    results_df = results_df.drop(results_df[results_df.value1 == 0].index)
    results_df = results_df.drop(results_df[results_df.average == -2].index)

    # hypothesis 1
    ok_results = results_df[results_df['average'] != -1]
    old_results = ok_results[ok_results['year'] <= 2011].count().sum()
    new_results = ok_results[ok_results['year'] > 2011].count().sum()

    old_new_comp = pd.DataFrame({'year': ['до 2011', 'после 2011'], 'count': [old_results, new_results]})
    old_new_comp.set_index('year', inplace=True)
    old_new_comp.plot(kind='pie', figsize=(6, 6), subplots=True)

    # hypothesis 2
    df_2 = results_df.drop(results_df[results_df.eventName == '3x3x3 Blind Old Style'].index)
    df_2 = df_2.drop(df_2[df_2.eventName == '3x3x3 Multi-Blind Old Style'].index)
    df_2 = df_2['eventName'].value_counts()

    df_2.plot(kind='bar', figsize=(7, 7))

    # hypothesis 3
    usa_comp_amount = competitions_df[competitions_df.countryName == 'United States'].count().sum()
    europe_comp_amount = competitions_df[competitions_df.continentId == '_Europe'].count().sum()
    usa_europe_df = pd.DataFrame({'country': ['Европа', 'США'], 'Количество соревнований': [europe_comp_amount, usa_comp_amount]})
    usa_europe_df.set_index('country', inplace=True)
    usa_europe_df.plot(kind='pie', subplots=True)

    # hypothesis 4
    df_4 = results_df.drop(results_df[results_df.year < 2004].index)
    df_4 = df_4[df_4['eventName'] == '3x3x3 Cube'].groupby('year')['average'].mean()
    df_4.plot()
    plt.xticks(np.arange(2004, 2016, 1))

    # hypothesis 5
    df_5 = results_df.drop(results_df[results_df.eventName == '3x3x3 Blind Old Style'].index)
    df_5 = df_5.drop(df_5[df_5.eventName == '3x3x3 Multi-Blind Old Style'].index)
    df_5 = df_5[df_5['average'] == -1].groupby('eventName')['average'].count().sort_values()
    df_5.plot(kind='pie', figsize=(7, 7))

    plt.show()


if __name__ == '__main__':
    main()
