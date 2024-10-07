import pandas as pd
import streamlit as st
dfstores= pd.read_csv("D:\\Python project\\Youtube Data\\DataFile\\Stores.csv",encoding='latin1')
st.write(dfstores.head())
#cols=['Zip Code','State Code','City']
#dfcustomers.drop(cols,inplace=True,axis=1)
st.write(dfstores.head())
st.write(dfstores.isnull().sum())

dfstores['Open Date']=pd.to_datetime(dfstores['Open Date'])
st.write(dfstores.dtypes)
#dfcustomers=dfcustomers.astype({'unit_cost':'float'})

y=[]
for i in range(len(dfstores)):
    x=tuple(dfstores.iloc[i])
    y.append(x)

st.write(y)

file=open('stores.txt','w')
for tuple in y:
    file.write(str(tuple)+','+'\n')
    
file.close()    
