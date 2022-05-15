import pandas as pd 
import numpy as np 
import streamlit as st



transactions = pd.read_csv('/Users/alanwu/Documents/Datasets/transactions.csv')
transactions.drop(['Labels', 'Notes'], axis = 1,inplace=True)
transactions['Date'] = pd.to_datetime(transactions['Date'], format='%m/%d/%Y')


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



febTransactions = getMonthlyTransactions('02','2022')
descriptions = transactions['Description']

i = 0
list = []
while i < len(transactions):
    if('Online Banking transfer' in descriptions[i]): 
        list.append(i)
    elif('LIU' in descriptions[i]): 
        list.append(i)
    i+=1
print(list)
transactions.drop(labels=list,inplace=True)
print(transactions['Category'].value_counts())