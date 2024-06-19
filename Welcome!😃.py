import streamlit as st
import pandas as pd

#import SessionState
st.set_page_config(layout="wide")


st.title("Retail Company Data")
st.markdown("Here you can review the data base created after ETL process/Aquí puedes consultar la base de datos creada después del proceso de ETL")

features = pd.read_csv('data/features_Delta.csv')
sales = pd.read_csv('data/sales_Delta.csv')
stores = pd.read_csv('data/stores_Delta.csv')

dataset = features.merge(sales, how='inner', on=['Store','Date', 'IsHoliday'])
dataset = dataset.merge(stores, how='inner', on='Store')

# Numero de entradas por hoja
N = 10


# A variable to keep track of which product we are currently displaying

if 'page_number' not in st.session_state:
    st.session_state['page_number'] = 0


last_page = (len(dataset) // N )-1

col1, col2 = st.columns(2)

with col1:
    prev = st.button('Previous')

with col2:
    next = st.button('Next')

if next:

    if st.session_state['page_number'] >= last_page:
        st.session_state['page_number'] = 0
                
    else:
        st.session_state['page_number'] += 1
        
if prev:

    if st.session_state['page_number'] - 1 <= -1:
        st.session_state['page_number'] = last_page

    else:
        st.session_state['page_number'] -= 1



# Get start and end indices of the next page of the dataframe
start_idx = st.session_state['page_number'] * N 
end_idx = (1 + st.session_state['page_number']) * N


# Index into the sub dataframe
sub_df = dataset.iloc[start_idx:end_idx]
st.write(sub_df)

