import pandas as pd
import matplotlib.pyplot as plt

results_df = pd.read_csv('WCA_export_Results.tsv', sep='\t')
competitions_df = pd.read_csv('WCA_export_Competitions.tsv', sep='\t')
events_df = pd.read_csv('WCA_export_Events.tsv', sep='\t')
round_types_df = pd.read_csv('WCA_export_RoundTypes.tsv', sep='\t')
persons_df = pd.read_csv('WCA_export_Persons.tsv', sep = '\t')
formats_df = pd.read_csv('WCA_export_Formats.tsv', sep = '\t')
countries_df = pd.read_csv('WCA_export_Countries.tsv', sep = '\t')