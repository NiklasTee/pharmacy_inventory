from database_helpers import *
import pandas as pd


for year in range(2004, 2022):

    df = pd.read_csv(f'../data/transactions_csv/peissen_{year}.csv', sep=';', encoding='utf-8')
    hersteller_unique, lager_unique, warengruppe_unique, auftrag_unique, arzneimittel_unique = extractTables(df)

    hersteller_unique.to_pickle(f'../data/tables_raw/hersteller/hersteller_{year}')
    lager_unique.to_pickle(f'../data/tables_raw/lager/lager_{year}')
    warengruppe_unique.to_pickle(f'../data/tables_raw/warengruppe/warengruppe_{year}')
    auftrag_unique.to_pickle(f'../data/tables_raw/auftrag/auftrag_{year}')
    arzneimittel_unique.to_pickle(f'../data/tables_raw/arzneimittel/arzneimittel_{year}')



