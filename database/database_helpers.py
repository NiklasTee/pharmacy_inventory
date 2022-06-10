import os
import pandas as pd


columns_hersteller = ['HerKue']
columns_lager = ['Lagerort']
columns_warengruppe = ['ATC-Warengruppe', 'ATC-Warengruppenbezeichnung 1', 'ATC-Warengruppenbezeichnung 2', 'ATC-Warengruppenbezeichnung 3']
columns_arzneimittel = ['PZN', 'Bezeichnung', 'HerKue', 'Darr', 'Menge', 'ATC-Warengruppe', 'ME', 'Rezeptpflichtig', 'Apothekenpflichtig', 'Lagerort']
columns_auftrag = ['Auftrag', 'Datum']

def extractTables (df):

    hersteller_df = df[columns_hersteller]
    lager_df = df[columns_lager]
    warengruppe_df = df[columns_warengruppe]
    arzneimittel_df = df[columns_arzneimittel]
    auftrag_df = df[columns_auftrag]

    hersteller_unique = hersteller_df.drop_duplicates()
    hersteller_unique.dropna(inplace=True)

    lager_unique = lager_df.drop_duplicates()
    lager_unique.dropna(inplace=True)

    warengruppe_unique = warengruppe_df.drop_duplicates()
    warengruppe_unique = warengruppe_unique[warengruppe_unique['ATC-Warengruppe'].notna()]

    auftrag_unique = auftrag_df.drop_duplicates()
    auftrag_unique.dropna(inplace=True)
    auftrag_unique['Auftrag'] = auftrag_unique['Auftrag'].astype('int32')

    arzneimittel_unique = arzneimittel_df.drop_duplicates(subset='PZN', keep='last')
    arzneimittel_unique = arzneimittel_unique[arzneimittel_unique['PZN'].notna()]
    arzneimittel_unique['PZN'] = arzneimittel_unique['PZN'].astype('int32')

    return hersteller_unique, lager_unique, warengruppe_unique, auftrag_unique, arzneimittel_unique


def mergeTables (table_name):

    table_files = os.listdir(f'../data/tables_raw/{table_name}/')
    table_dfs = []
    for file in table_files:
        table_dfs.append(pd.read_pickle(os.path.join(f'../data/tables_raw/{table_name}/', file)))
    table_df = pd.concat(table_dfs)

    return table_df


def preprocessVerfall (date_str):

    try:
        date_str_preprocessed = date_str.split(":")[0]  # One expiration date is assumed for all drugs

    except AttributeError:
        date_str_preprocessed = "01.1999"

    return date_str_preprocessed


def enrichLager (lagerort_str, bezeichnung_dict):

    lagerort_bezeichnungen = []
    lagerorte = list(lagerort_str)
    for ort in lagerorte:
        try:
            lagerort_bezeichnungen.append(bezeichnung_dict[ort])
        except KeyError:
            pass

    if lagerort_str == "BTM":
        lagerort_bezeichnungen = ["Betäubungsmittel"]

    return ' '.join(lagerort_bezeichnungen)


