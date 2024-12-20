import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np


# import matplotlib.pyplot as plt
# import seaborn as sns
with st.sidebar:
    st.title('DASHBOARD')
#Charger les Données :
holidays_events = pd.read_csv('holidays_events.csv', delimiter=",")
train = pd.read_csv('train.csv', delimiter=",")
test = pd.read_csv('test.csv', delimiter=",")
stores = pd.read_csv('stores.csv', delimiter=",")
oil = pd.read_csv('oil.csv', delimiter=",")
sample_submission = pd.read_csv('sample_submission.csv', delimiter=",")
transactions = pd.read_csv('transactions.csv', delimiter=",")



train['date'] = pd.to_datetime(train['date'])  # Convertir la colonne 'date' en datetime
oil['date'] = pd.to_datetime(train['date'])  # Convertir la colonne 'date' en datetime
sample_submission['date'] = pd.to_datetime(train['date'])  # Convertir la colonne 'date' en datetime
transactions['date'] = pd.to_datetime(train['date'])  # Convertir la colonne 'date' en datetime
test['date'] = pd.to_datetime(train['date'])  # Convertir la colonne 'date' en datetime
holidays_events['date'] = pd.to_datetime(train['date'])  # Convertir la colonne 'date' en datetime
stores['date'] = pd.to_datetime(train['date'])  # Convertir la colonne 'date' en datetime

# Créer la sidebar


st.sidebar.title("Filtres")

chart = alt.Chart(filtered_data).mark_bar().encode(
    alt.X("sales:Q", bin=True),
    alt.Y("count()")
).properties(
    title=f"Distribution des ventes pour {selected_month}/{selected_year}"
)
st.altair_chart(chart, use_container_width=True)

