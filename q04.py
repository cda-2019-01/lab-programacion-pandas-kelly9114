##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
import numpy as np

df0 = pd.read_csv('tablas/tbl0.tsv', sep='\t')
df1 = pd.read_csv('tablas/tbl1.tsv', sep='\t')
df2 = pd.read_csv('tablas/tbl2.tsv', sep='\t')

uniques = df1['_c4'].unique()
x = []
for f in uniques:
    x.append(f.upper())
x = sorted(x)
x
