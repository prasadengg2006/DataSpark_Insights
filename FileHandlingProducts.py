import pandas as pd
import streamlit as st
import warnings as warning
dfProducts= pd.read_csv("D:\\Python project\\Youtube Data\\DataFile\\Products.csv")
dfProducts['Unit_Cost']=dfProducts['Unit Cost USD'].str.replace('$','').str.replace(',','')
dfProducts['Unit_Price']=dfProducts['Unit Price USD'].str.replace('$','').str.replace(',','')

st.write(dfProducts.head())
cols=['SubcategoryKey','CategoryKey','Unit Cost USD','Unit Price USD']
dfProducts.drop(cols,inplace=True,axis=1)
st.write(dfProducts.head())
st.write(dfProducts.isnull().sum())

dfProducts['Unit_Cost']=pd.to_numeric(dfProducts['Unit_Cost']) 
dfProducts['Unit_Price']=pd.to_numeric(dfProducts['Unit_Price']) 

titles=list(dfProducts.columns)
#dfProducts=dfProducts.astype({'Unit Cost USD':'float','Unit Price USD':'float'})
st.write(dfProducts.dtypes)
titles[4],titles[5],titles[6],titles[7]=titles[6],titles[7],titles[4],titles[5]
dfProducts=dfProducts[titles]
st.write(dfProducts)
y=[]
for i in range(len(dfProducts)):
    x=tuple(dfProducts.iloc[i])
    y.append(x)

st.write(y)

file=open('products.txt','w')
for tuple in y:
    file.write(str(tuple)+','+'\n')
    
file.close()    
