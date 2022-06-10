from database_helpers import preprocessVerfall
import datetime as dt
import numpy as np
import pandas as pd


arzneimittel_df = pd.read_csv(f'../data/tables_intermediate/arzneimittel.csv', sep=',', encoding='utf-8')
auftrag_df = pd.read_csv(f'../data/tables_intermediate/auftrag.csv', sep=',', encoding='utf-8')
hersteller_df = pd.read_csv(f'../data/tables_intermediate/hersteller.csv', sep=',', encoding='utf-8')
lager_df = pd.read_csv(f'../data/tables_intermediate/lager.csv', sep=',', encoding='utf-8')
transaktion_df = pd.read_csv(f'../data/tables_intermediate/transaktion.csv', sep=',', encoding='utf-8')
warengruppe_df = pd.read_csv(f'../data/tables_intermediate/warengruppe.csv', sep=',', encoding='utf-8')

arzneimittel_df['Rezeptpflichtig'] = arzneimittel_df['Rezeptpflichtig'].apply(lambda x: True if x == "Ja" else False)
arzneimittel_df['Apothekenpflichtig'] = arzneimittel_df['Apothekenpflichtig'].apply(lambda x: True if x == "Ja" else False)
arzneimittel_df.astype({
    'PZN': 'int64',
    'Bezeichnung': 'object',
    'HerKue': 'object',
    'Darr': 'object',
    'Menge': 'object',
    'ATC-Warengruppe': 'object',
    'ME': 'object',
    'Rezeptpflichtig': 'bool',
    'Apothekenpflichtig': 'bool',
    'Lagerort': 'object'

}, copy=False)

arzneimittel_df.drop_duplicates(subset='PZN', keep='last', inplace=True)
arzneimittel_df.to_csv('../data/tables_preprocessed/arzneimittel.csv', encoding='utf-8', index=False)

auftrag_df['Datum'] = pd.to_datetime(auftrag_df['Datum'], format='%d.%m.%Y')
auftrag_df.astype({
    'Auftrag': 'int64',
    'Datum': 'datetime64'
}, copy=False)
auftrag_df.to_csv('../data/tables_preprocessed/auftrag.csv', encoding='utf-8', index=False)

hersteller_df.astype({'HerKue': 'object'}, copy=False)
hersteller_df.to_csv('../data/tables_preprocessed/hersteller.csv', encoding='utf-8', index=False)

lager_df.astype({'Lagerort': 'object'}, copy=False)
lager_df.to_csv('../data/tables_preprocessed/lager.csv', encoding='utf-8', index=False)

transaktion_df['Retoure'] = transaktion_df['Retoure'].apply(lambda x: True if x == "Ja" else False)
transaktion_df['Datum'] = pd.to_datetime(transaktion_df['Datum'], format='%d.%m.%Y')
transaktion_df['Uhrzeit'] = pd.to_datetime(transaktion_df['Uhrzeit'], format='%H:%M').dt.time
transaktion_df['Verfalldaten'] = transaktion_df['Verfalldaten'].map(lambda x: preprocessVerfall(x))
transaktion_df['Verfalldaten'] = pd.to_datetime(transaktion_df['Verfalldaten'], format='%m.%Y')
transaktion_df['Verfalldaten'] = transaktion_df['Verfalldaten'].replace(pd.to_datetime('01-01-1999', format='%d-%m-%Y'), np.nan)
transaktion_df['Nachlieferungsmenge'] = transaktion_df['Nachlieferungsmenge'].fillna(0)
transaktion_df['Anzahl'] = transaktion_df['Anzahl'].astype(int)
transaktion_df['Nachlieferungsmenge'] = transaktion_df['Nachlieferungsmenge'].astype(int)
transaktion_df = transaktion_df[transaktion_df['PZN'] >= 0]

transaktion_df.astype({
    'Auftrag': 'int64',
    'Datum': 'datetime64',
    'Uhrzeit': 'object',
    'PZN': 'int64',
    'Anzahl': 'int64',
    'Retoure': 'bool',
    'Verfalldaten': 'datetime64',
    'Nachlieferungsmenge': 'int64'
}, copy=False)


transaktion_df.to_csv('../data/tables_preprocessed/transaktion.csv', encoding='utf-8', index=False)

warengruppe_df.astype({
    'ATC-Warengruppe': 'object',
    'ATC-Warengruppenbezeichnung 1': 'object',
    'ATC-Warengruppenbezeichnung 2': 'object',
    'ATC-Warengruppenbezeichnung 3': 'object',
}, copy=False)

warengruppe_df.to_csv('../data/tables_preprocessed/warengruppe.csv', encoding='utf-8', index=False)