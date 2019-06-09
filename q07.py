##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 

import pandas as pd

df0 = pd.read_csv('tablas/tbl0.tsv', sep='\t')
df1 = pd.read_csv('tablas/tbl1.tsv', sep='\t')
df2 = pd.read_csv('tablas/tbl2.tsv', sep='\t')

df0 ['suma']= df0['_c0'] + df0['_c2']


