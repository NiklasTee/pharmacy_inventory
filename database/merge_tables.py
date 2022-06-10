from database_helpers import *
import pandas as pd


hersteller_df = mergeTables('hersteller')
hersteller_unique = hersteller_df['HerKue'].drop_duplicates()
hersteller_unique.sort_values(inplace=True)
hersteller_unique.to_csv('../data/tables_intermediate/hersteller.csv', encoding='utf-8', index=False)


lager_df = mergeTables('lager')
lager_unique = lager_df['Lagerort'].drop_duplicates()
lager_unique.sort_values(inplace=True)
lager_unique.to_csv('../data/tables_intermediate/lager.csv', encoding='utf-8', index=False)

warengruppe_df = mergeTables('warengruppe')
warengruppe_unique = warengruppe_df.drop_duplicates()
warengruppe_unique.sort_values('ATC-Warengruppe', inplace=True)
warengruppe_unique.to_csv('../data/tables_intermediate/warengruppe.csv', encoding='utf-8', index=False)

auftrag_df = mergeTables('auftrag')
auftrag_unique = auftrag_df.drop_duplicates()
auftrag_unique.sort_values('Auftrag', inplace=True)
auftrag_unique.to_csv('../data/tables_intermediate/auftrag.csv', encoding='utf-8', index=False)

arzneimittel_df = mergeTables('arzneimittel')
arzneimittel_unique = arzneimittel_df.drop_duplicates()
arzneimittel_unique = arzneimittel_unique[arzneimittel_unique.PZN > 0]
arzneimittel_unique.sort_values('PZN', inplace=True)
arzneimittel_unique.to_csv('../data/tables_intermediate/arzneimittel.csv', encoding='utf-8', index=False)


