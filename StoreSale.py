import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np
# import plotly.express as px

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


# Calculer les ventes totales par magasin
store_sales = train.groupby('store_nbr')['sales'].sum().reset_index()

# Créer le graphique en donut avec Plotly Express
fig = px.pie(
    store_sales, 
    values='sales', 
    names='store_nbr', 
    title="Répartition des ventes par magasin",
    hole=0.4  # Définir la taille du trou pour créer un donut
)

# Afficher le graphique dans Streamlit
st.altair_chart(donut_chart, use_container_width=True)
