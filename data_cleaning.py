import pandas as pd
import numpy as np
missing_values = ["n.a.","NA","n/a", "na", "nan"]
#df=pd.read_csv("Consumption.csv", encoding='utf-8-sig',na_values = missing_values)
df=pd.read_csv("Production.csv", encoding='utf-8-sig',na_values = missing_values)
df.dropna( how='all')
df.dropna( how='any', subset=['Full_solar'])
#df.dropna( how='any', subset=['Energy'])
df.dropna( thresh=7)
df.fillna(method='ffill', inplace=True)
# df.to_csv ('..\dataset\Production.csv', index = False, header=True)
