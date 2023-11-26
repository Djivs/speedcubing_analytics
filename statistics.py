def describe_results(df):
    print(df['best'].describe())
    print(df['average'].describe())
    print(df['pos'].describe())
    print(df['year'].describe())


def corr(df):
    numeric_col = ['best', 'average', 'pos', 'year']
    print(df.loc[:, numeric_col].corr())
