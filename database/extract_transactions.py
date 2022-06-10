from database_helpers import *
import pandas as pd

columns_transactions = [
    'Auftrag',
    'Datum',
    'Uhrzeit',
    'PZN',
    'Anzahl',
    'Retoure',
    'Verfalldaten',
    'Nachlieferungsmenge'
]

transaction_dfs = []


for year in range(2004, 2022):
    annual_df = pd.read_csv(f'../data/transactions_csv/peissen_{year}.csv', sep=';', encoding='utf-8')
    annual_transactions_df = annual_df[columns_transactions]
    annual_transactions_df = annual_transactions_df[annual_transactions_df.PZN.notna()]
    annual_transactions_df = annual_transactions_df[annual_transactions_df.Auftrag.notna()]
    annual_transactions_df[['Auftrag', 'PZN']] = annual_transactions_df[['Auftrag', 'PZN']].astype('int32')
    transaction_dfs.append(annual_transactions_df)

transaction_df = pd.concat(transaction_dfs)
transaction_df.to_csv('../data/tables_intermediate/transaktion.csv', encoding='utf-8', index=False)

