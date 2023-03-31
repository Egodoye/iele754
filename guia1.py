import pandas as pd
import seaborn  as sns

df1 = pd.read_csv("/Users/eduardogodoy/Desktop/PYA/2020_temperatura_aire_ceaza.csv")
df1['time'] = pd.to_datetime(df1.time, format='%Y-%m-%d %H:%M:%S')

df10 = df1.loc[(df1['time'].dt.month==3)] 
df10

df2 = pd.read_csv("/Users/eduardogodoy/Desktop/PYA/2023_temperatura_aire_ceaza.csv")
df2['time'] = pd.to_datetime(df2.time, format='%Y-%m-%d %H:%M:%S')

df20 = df2.loc[(df2['time'].dt.month==3)] 
df20

sns.kdeplot(df10.prom)
sns.kdeplot(df20.prom)