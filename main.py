import pandas as pd
import matplotlib.pyplot as plt

results_df = pd.read_csv('WCA_export_Results.tsv', sep='\t')
competitions_df = pd.read_csv('WCA_export_Competitions.tsv', sep='\t')
events_df = pd.read_csv('WCA_export_Events.tsv', sep='\t')
round_types_df = pd.read_csv('WCA_export_RoundTypes.tsv', sep='\t')
persons_df = pd.read_csv('WCA_export_Persons.tsv', sep='\t')
formats_df = pd.read_csv('WCA_export_Formats.tsv', sep='\t')
countries_df = pd.read_csv('WCA_export_Countries.tsv', sep='\t')

persons_df = pd.merge(persons_df, countries_df, on='countryId', how='inner')
competitions_df = pd.merge(competitions_df, countries_df, on='countryId', how='inner')

results_df = pd.merge(results_df, competitions_df, on='competitionId', how='inner')
results_df = pd.merge(results_df, events_df, on='eventId', how='inner')
results_df = pd.merge(results_df, round_types_df, on='roundTypeId', how='inner')
results_df = pd.merge(results_df, persons_df, on='personId', how='inner')
results_df = pd.merge(results_df, formats_df, on='formatId', how='inner')

results_df.drop_duplicates(subset=['competitionId', 'personId', 'roundTypeId', 'eventId', 'value1', 'value2', 'value3',
                                   'value4', 'value5'])

results_df = results_df.drop(results_df[results_df.value1 == 0].index)

old_results = results_df[results_df['year'] <= 2011].count().sum()
new_results = results_df[results_df['year'] > 2011].count().sum()

old_new_comp = pd.DataFrame({'year': ['2007-2011', '2012-2016'], 'count': [old_results, new_results]})
# old_new_comp.set_index('year', inplace=True)
# print(old_new_comp)
# old_new_comp.plot(kind='pie', figsize=(6, 6), subplots=True)

timed_results_df = results_df[results_df['format'] == 'time']['eventName'].value_counts()
timed_results_df.plot(kind='bar', figsize=(7, 7))

plt.show()
