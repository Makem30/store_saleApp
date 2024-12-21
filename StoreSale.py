import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np

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

# Create two columns
col1, col2 = st.columns([0.5,0.4],gap="large")

with col2:
# Calculer les ventes totales par magasin
    store_sales = train.groupby('store_nbr')['sales'].sum().reset_index()
    
    # Créer le graphique en donut avec Altair
    chart = alt.Chart(store_sales).mark_arc(innerRadius=50).encode(
        theta="sales:Q",
        color="store_nbr:N"
    ).properties(
        title="Répartition des ventes par magasin"
    )
    
    # Afficher le graphique dans Streamlit
    st.altair_chart(chart, use_container_width=True)


# ---------------------------------------------------------------------
with col1:
# Calculer les ventes totales par magasin
    store_sales = train.groupby('store_nbr')['sales'].sum().reset_index()
    
    # Trier les magasins par ventes totales et sélectionner le top 10
    top_10_stores = store_sales.sort_values(by='sales', ascending=False).head(10)
    
    # Créer l'histogramme avec Altair
    chart = alt.Chart(top_10_stores).mark_bar().encode(
        x=alt.X('store_nbr:N', title="Magasin"),  # 'N' pour type nominal (catégoriel)
        y=alt.Y('sales:Q', title="Ventes totales")   # 'Q' pour type quantitatif
    ).properties(
        title="Top 10 des magasins avec les meilleures ventes"
    )
    
    
    # Afficher l'histogramme dans Streamlit
    st.altair_chart(chart, use_container_width=True)


#---------------------------------------------------------------------------------------

# Sidebar pour la sélection de l'année et du mois
st.sidebar.title("Filtres")
selected_year = st.sidebar.selectbox("Sélectionner l'année", train['date'].dt.year.unique())
selected_month = st.sidebar.selectbox("Sélectionner le mois", train['date'].dt.month.unique())

# Filtrer les données en fonction des sélections
filtered_data = train[
    (train['date'].dt.year == selected_year) & (train['date'].dt.month == selected_month)
]

# Calculer les ventes totales par jour pour le mois sélectionné
daily_sales = filtered_data.groupby(filtered_data['date'].dt.day)['sales'].sum().reset_index()

# Créer l'histogramme coloré avec Altair
chart = alt.Chart(daily_sales).mark_bar().encode(
    x=alt.X('date:T', title="Jour du mois"),  # 'T' pour type temporel
    y=alt.Y('sales:Q', title="Ventes totales"),
    color=alt.Color('sales:Q', scale=alt.Scale(scheme='viridis'))  # Colorer par ventes totales
).properties(
    title=f"Ventes totales pour {selected_month}/{selected_year}"
)

# Afficher l'histogramme dans Streamlit
st.altair_chart(chart, use_container_width=True)

#---------------------------------------------------------------------------------------
# Normaliser les ventes (vous pouvez ajuster la méthode de normalisation si nécessaire)
train['sales_scaled'] = (train['sales'] - train['sales'].min()) / (train['sales'].max() - train['sales'].min())

# Calculer les ventes moyennes normalisées par magasin
avg_sales_by_store = train.groupby('store_nbr')['sales_scaled'].mean().reset_index()

# Créer le graphique avec Altair
chart = alt.Chart(avg_sales_by_store).mark_bar().encode(
    x=alt.X('store_nbr:N', title="Magasin"),
    y=alt.Y('sales_scaled:Q', title="Ventes moyennes normalisées"),
    color=alt.Color('sales_scaled:Q', scale=alt.Scale(scheme='viridis'))  # Colorer par ventes normalisées
).properties(
    title="Visualisation des ventes moyennes par magasin normalisées"
)

# Afficher le graphique dans Streamlit
st.altair_chart(chart, use_container_width=True)
#---------------------------------------------------------------------------------------
# Sidebar pour la sélection du magasin
st.sidebar.title("Sélection du magasin")
selected_store = st.sidebar.selectbox("Magasin", train['store_nbr'].unique())

# Filtrer les données pour le magasin sélectionné
filtered_data = train[train['store_nbr'] == selected_store]

# Obtenir la liste des produits uniques pour le magasin sélectionné
products = filtered_data['family'].unique()  # Utilisez 'family' pour les produits

# Afficher la liste des produits
st.title(f"Liste des produits pour le magasin {selected_store}")
st.write(products)  # Ou utilisez st.table(products) pour un affichage en tableau
