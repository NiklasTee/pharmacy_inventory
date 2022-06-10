from database_helpers import enrichLager
import pandas as pd


lager_bezeichnung = {
    "C": "Sichtwahl",
    "G": "Generalalphabet",
    "F": "Freiwahl",
    "N": "Novität",
    "R": "Rezeptur",
    "V": "Verbandstoff",
    "X": "Nicht auf Lager",
    "K": "Kühlschrank"
}

lager_df = pd.read_csv(f'../data/tables_preprocessed/lager.csv', encoding='utf-8')

lager_df['LagerortName'] = lager_df['Lagerort'].map(lambda x: enrichLager(x, lager_bezeichnung))

lager_df.astype({'LagerortName': 'object'}, copy=False)
lager_df.to_csv('../data/tables_preprocessed/lager.csv', encoding='utf-8', index=False)

