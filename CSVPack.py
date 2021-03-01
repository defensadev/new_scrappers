import pandas as pd
import glob, os

def clean_df(df):
    new_columns = ['CaseNumber', 'CaseStatus', 'DefendantName', 'DefendantAddr1', 'DefendantAddr2', 'DefendantCity', 'DefendantState', 'DefendantZIP', 'HearingDate']
    columns = ['Case Number', 'Case Status ', 'Defendant Name', 'Defendant Addr Line 1 ', 'Defendant Addr Line 2 ', 'Defendant Addr City ', 'Defendant Addr State', 'Defendant Addr ZIP 1', 'Next Hearing Date']
    columns_to_delete = set(df.columns) - set(columns)
    df = df.drop(columns_to_delete, axis=1)
    df = df.rename(columns=dict(zip(columns, new_columns)))

    return df


def GetAlldfs():
    files = glob.glob('tmp_csvs/*.csv')
    harrisnames = map(os.path.basename, files)
    county_names = [harrisname.split('-')[0] for harrisname in harrisnames]

    dfs = []
    for file, county in zip(files, county_names):
        df = pd.read_csv(file, error_bad_lines=False)
        df = clean_df(df)
        df['County'] = county
        dfs.append(df)

    df = pd.concat(dfs)

    df.to_csv('All.csv', index=False)

if __name__ == '__main__':
    GetAlldfs()