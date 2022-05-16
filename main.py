import pandas as pd 
import streamlit as st
from plotly_calplot import calplot
import plotly.express as px


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




#calendar heatmap
fig = calplot(
   transactions,
    x='Date',
    y='Amount',
    title="Spending Calendar"
)

#barplot
catNames = transactions['Category'].value_counts().index.tolist()
catCounts = transactions['Category'].value_counts().tolist()
categoryData = {'Category':catNames,'Counts':catCounts}
df = pd.DataFrame(categoryData)
fig2 = px.bar(df,x='Counts',y='Category' ,orientation='h',title='Spending By Category')



sum = transactions['Amount'].sum()
transactionsMay = getMonthlyTransactions('05','2022')
#orangizing streamlit app
st.header("Alan's Spending Habits")

a1,a2 = st.columns(2) 
a1.metric('Total Spending', "$"+str(sum))
a2.metric('Amount Spent In May', '$'+str(transactionsMay['Amount'].sum()))
st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(fig2)