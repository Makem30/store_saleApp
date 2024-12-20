import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

#Charger les Données :
holidays_events = pd.read_csv('holidays_events.csv', delimiter=",")
# train = pd.read_csv('train.csv', delimiter=",")
test = pd.read_csv('test.csv', delimiter=",")
stores = pd.read_csv('stores.csv', delimiter=",")
oil = pd.read_csv('oil.csv', delimiter=",")
sample_submission = pd.read_csv('sample_submission.csv', delimiter=",")
transactions = pd.read_csv('transactions.csv', delimiter=",")


# Charger les données
train = pd.read_csv('train.csv', delimiter=",") 
train['date'] = pd.to_datetime(train['date'])  # Convertir la colonne 'date' en datetime

# Créer la sidebar
st.sidebar.title("Filtres")
selected_year = st.sidebar.selectbox("Sélectionner l'année", train['date'].dt.year.unique())
selected_month = st.sidebar.selectbox("Sélectionner le mois", train['date'].dt.month.unique())


# Filtrer les données en fonction des sélections
filtered_data = train[
    (train['date'].dt.year == selected_year) & (train['date'].dt.month == selected_month)
]

# Créer les graphiques
if st.sidebar.button("Afficher les ventes par mois"):
    fig, ax = plt.subplots(figsize=(10, 6))  
    sns.lineplot(x='date', y='sales', data=filtered_data, ax=ax) 
    ax.set_title(f"Ventes pour {selected_month}/{selected_year}") 
    st.pyplot(fig) 

if st.sidebar.button("Afficher les ventes par an"):
    yearly_sales = train.groupby(train['date'].dt.year)['sales'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='date', y='sales', data=yearly_sales, ax=ax)
    ax.set_title("Ventes annuelles")
    st.pyplot(fig)




# import zipfile
# with zipfile.ZipFile("train.zip", "r") as zip_ref:
#     # zip_ref.extractall("train.zip")
#     train = pd.read_csv("train.csv")














# Create two columns
# col1, col2 = st.columns([0.5,0.4],gap="large")

# with col1:

  #Content for the first column
# with col2:

# with st.sidebar:
#   st.title('DASHBOARD')
#   st.sidebar.title("Comparateur de données")
