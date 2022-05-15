import pandas as pd 
import numpy as np 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sb
import calplot 
from plotly_calplot import calplot


pd.set_option('display.max_columns',None)
#data set of monthly transactions
transactions = pd.read_csv('/Users/alanwu/Documents/Datasets/transactions.csv')

#deleting empty columns and clean data
transactions.drop(['Labels', 'Notes'], axis = 1,inplace=True)
transactions['Date'] = pd.to_datetime(transactions['Date'], format='%m/%d/%Y')

#deleting incoming transfer 
descriptions = transactions['Description']
i = 0
list = []
while i < len(transactions):
    if('Online Banking transfer' in descriptions[i]): 
        list.append(i)
    elif('LIU' in descriptions[i]): 
        list.append(i)
    i+=1
transactions.drop(labels=list,inplace=True)
transactions.reset_index(drop=True,inplace=True)
transactions['Num_Transactions'] = 1
print(transactions.head())
#returns a subset of monthly transactions 
def getMonthlyTransactions(month, year):
    startDay = '01'
    endDay = '30'
    if(month == '02'): 
        endDay = '28'
    elif(month=='01' or month == '03' or month =='05' or month =='07' or month=='08' or month=='10' or month=='12'):
        endDay = '31'
    startDate = year + '-' + month + '-' + startDay
    endDate = year + '-' + month + '-' + endDay
    return transactions.loc[(transactions['Date'] >= startDate) & (transactions['Date'] <=endDate)] 
#transactions.set_index('Date',inplace=True)
#col = 'Amount'
#cmap = sb.light_palette('#912CEE',as_cmap=True)
#calplot.calplot(transactions[col],how='sum',colorbar=False,cmap=cmap)




fig = calplot(
   transactions,
    x='Date',
    y='Amount',
    title="Spending Calendar"
)
#orangizing streamlit app
st.header("Alan's Spending Habits")
st.plotly_chart(fig, use_container_width=True)