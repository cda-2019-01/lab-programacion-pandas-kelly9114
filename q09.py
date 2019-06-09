##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 

import pandas as pd

df0 = pd.read_csv('tablas/tbl0.tsv', sep='\t')
df1 = pd.read_csv('tablas/tbl1.tsv', sep='\t')
df2 = pd.read_csv('tablas/tbl2.tsv', sep='\t')

dfx = df0.groupby('_c1')['_c2'].apply(list)

df = pd.DataFrame()
df['_c1'] = dfx.keys()
df['_c2'] = [x for x in dfx]

df['_c2'] = [":".join(str(v) for v in sorted(x)) for x in df['_c2']]

df