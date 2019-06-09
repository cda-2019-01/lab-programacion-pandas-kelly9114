##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 

import pandas as pd

df0 = pd.read_csv('tablas/tbl0.tsv', sep='\t')
df1 = pd.read_csv('tablas/tbl1.tsv', sep='\t')
df2 = pd.read_csv('tablas/tbl2.tsv', sep='\t')

dfx = df1.groupby('_c0')['_c4'].apply(list)

df = pd.DataFrame()
df['_c0'] = dfx.keys()
df['lista'] = [x for x in dfx]

df['lista'] = [",".join(str(v) for v in sorted(x)) for x in df['lista']]

df