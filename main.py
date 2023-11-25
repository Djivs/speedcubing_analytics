import pandas as pd
import matplotlib.pyplot as plt

import hypotheses as hp


def clear(results_df):
    results_df.drop_duplicates(
        subset=['competitionId', 'personId', 'roundTypeId', 'eventId', 'value1', 'value2', 'value3',
                'value4', 'value5'])

    results_df = results_df.drop(results_df[results_df.value1 == 0].index)
    results_df = results_df.drop(results_df[results_df.average == -2].index)
    return results_df


def main():
    # load data
    results_df = pd.read_csv('tsv/WCA_export_Results.tsv', sep='\t')
    competitions_df = pd.read_csv('tsv/WCA_export_Competitions.tsv', sep='\t')
    events_df = pd.read_csv('tsv/WCA_export_Events.tsv', sep='\t')
    round_types_df = pd.read_csv('tsv/WCA_export_RoundTypes.tsv', sep='\t')
    persons_df = pd.read_csv('tsv/WCA_export_Persons.tsv', sep='\t')
    formats_df = pd.read_csv('tsv/WCA_export_Formats.tsv', sep='\t')
    countries_df = pd.read_csv('tsv/WCA_export_Countries.tsv', sep='\t')

    # merge data
    persons_df = pd.merge(persons_df, countries_df, on='countryId', how='inner')
    competitions_df = pd.merge(competitions_df, countries_df, on='countryId', how='inner')

    results_df = pd.merge(results_df, competitions_df, on='competitionId', how='inner')
    results_df = pd.merge(results_df, events_df, on='eventId', how='inner')
    results_df = pd.merge(results_df, round_types_df, on='roundTypeId', how='inner')
    results_df = pd.merge(results_df, persons_df, on='personId', how='inner')
    results_df = pd.merge(results_df, formats_df, on='formatId', how='inner')

    # clean data
    results_df = clear(results_df)

    # run hypothesis
    hp.h1(results_df)

    # show plot
    plt.show()


if __name__ == '__main__':
    main()
