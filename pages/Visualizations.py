import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



st.set_page_config(
    layout="wide",
    page_title="Features",
    page_icon="👋",
)

fig = plt.figure(figsize=(16,7))

features = pd.read_csv('data/features_Delta.csv')
sales = pd.read_csv('data/sales_Delta.csv')
stores = pd.read_csv('data/stores_Delta.csv')

dataset = features.merge(sales, how='inner', on=['Store','Date', 'IsHoliday'])
dataset = dataset.merge(stores, how='inner', on='Store')
dataset['Date']=pd.to_datetime(dataset['Date'], format='%Y/%m/%d')

sns.lineplot(data = dataset[dataset['IsHoliday']==True], x='Date', y='Weekly_Sales')


#Plotting media sum of sales to compare no markdowns vs markdowns
mean_markdown_holidays = dataset[(dataset['IsHoliday']==True)|(dataset['Date']>='2011-11-11')]['Weekly_Sales'].mean()
mean_no_markdown = dataset[(dataset['IsHoliday']==True)|(dataset['Date']<='2011-11-11')]['Weekly_Sales'].mean()

plt.axhline(mean_markdown_holidays, linestyle='--',c='r',label= 'Promedio de ventas con MarkDown')
plt.axhline(mean_no_markdown, linestyle='--',c='g',label= 'Promedio de ventas sin MarkDown')
plt.axvline(pd.to_datetime('2011-11-11', format = '%Y-%m-%d'), c='m',linestyle='--',label= 'Introducción de MarkDowns')



plt.title('Weekly Sales vs Date in Holidays')
plt.legend()
plt.grid()

st.pyplot(fig)
