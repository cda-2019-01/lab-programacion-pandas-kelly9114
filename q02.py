##
## Imprima el promedio de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
import pandas as pd

df0 = pd.read_csv('tablas/tbl0.tsv', sep='\t')
df1 = pd.read_csv('tablas/tbl1.tsv', sep='\t')
df2 = pd.read_csv('tablas/tbl2.tsv', sep='\t')

df0.groupby('_c1').mean()['_c2']
