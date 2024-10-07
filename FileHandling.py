import pandas as pd
import streamlit as st
dfcustomers= pd.read_csv("D:\\Python project\\Youtube Data\\DataFile\\Customers.csv",encoding='latin1')
st.write(dfcustomers.head())
cols=['Zip Code','State Code','City']
dfcustomers.drop(cols,inplace=True,axis=1)
st.write(dfcustomers.head())
st.write(dfcustomers.isnull().sum())

dfcustomers['Birthday']=pd.to_datetime(dfcustomers['Birthday'])
#st.write(dfcustomers.dtypes)
#dfcustomers=dfcustomers.astype({'unit_cost':'float'})

y=[]
for i in range(len(dfcustomers)):
    x=tuple(dfcustomers.iloc[i])
    y.append(x)

st.write(y)

file=open('customers.txt','w')
for tuple in y:
    file.write(str(tuple)+',')

file.close()    
