import pandas as pd
import numpy as np
df=pd.read_csv("../dataset/consumption.csv", encoding='utf-8-sig')
df['day_of_number'] = pd.to_datetime(df["date"], utc=True).dt.dayofweek
df['duration'] = pd.to_datetime(df['date'],utc=True).dt.hour
df['Month']=pd.to_datetime(df['date'], utc=True).dt.month
df["Day"]=pd.to_datetime(df["date"], utc=True).dt.day
df['hour_sin'] = np.sin(2 * np.pi * df['duration']/23.0)
df['hour_cos'] = np.cos(2 * np.pi * df['duration']/23.0)
df['day_of_week_sin'] = np.sin(2 * np.pi * df['day_of_number']/6.0)
df['day_of_week_cos'] = np.cos(2 * np.pi * df['day_of_number']/6.0)
df['Month_sin'] = np.sin(2 * np.pi * df['Month']/12.0)
df['Month_cos'] = np.cos(2 * np.pi * df['Month']/12.0)
df['day_sin'] = np.sin(2 * np.pi * df["Day"]/365.0)
df['day_cos'] = np.cos(2 * np.pi * df["Day"]/365.0)
print(df['duration'])
