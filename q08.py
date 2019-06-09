##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 

import pandas as pd

df0 = pd.read_csv('tablas/tbl0.tsv', sep='\t')
df1 = pd.read_csv('tablas/tbl1.tsv', sep='\t')
df2 = pd.read_csv('tablas/tbl2.tsv', sep='\t')

df0['ano'] = [i.split('-')[0] for i in df0['_c3']]

df0.head()