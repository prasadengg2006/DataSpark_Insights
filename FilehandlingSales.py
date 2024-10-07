import pandas as pd
import streamlit as st
dfsales= pd.read_csv("D:\\Python project\\Youtube Data\\DataFile\\Sales.csv",encoding='latin1')
st.write(dfsales.head())
#cols=['Zip Code','State Code','City']
#dfcustomers.drop(cols,inplace=True,axis=1)
st.write(dfsales.head())
st.write(dfsales.isnull().sum())

dfsales['OrderDate']=pd.to_datetime(dfsales['OrderDate'])
st.write(dfsales.dtypes)
#dfcustomers=dfcustomers.astype({'unit_cost':'float'})

y=[]
for i in range(len(dfsales)):
    x=tuple(dfsales.iloc[i])
    y.append(x)

st.write(y)

file=open('saless.txt','w')
for tuple in y:
    file.write(str(tuple)+','+'\n')
    
file.close()    
