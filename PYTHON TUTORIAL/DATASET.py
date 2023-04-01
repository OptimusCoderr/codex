#PANDA CSV FILES
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.impute import SimpleImputer
df=pd.read_csv('C:/Users/User/Downloads/index.csv')
#h=df.head(10)
#print(h)
x=df.drop(['location_key'],axis=1,inplace=True)
print(df.head())
df.rename(columns={'place_id':'PL ID','aggregation_level':'AGG_LEVEL'},inplace=True)
print(df.head())
print(df.describe())
print(df.info())
df=df.fillna('NA')
print(df)
print(df.info())
print(df.head(10))
df2=df.groupby(['country_name','AGG_LEVEL'])[['wikidata_id','country_code']].sum().reset_index()
print(df2)
df3=df2[df2['AGG_LEVEL']>0]
country_name=df3['country_name'].unique()
print(len(country_name))