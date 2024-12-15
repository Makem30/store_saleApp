import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import joblib

# Charger les données et le modèle
@st.cache
def load_data():
    # Simule un chargement de données pour la démo (remplace par tes données finales)
    data = pd.read_csv("train.csv")  # Charge tes données
    data['date'] = pd.to_datetime(data['date'])
    return data

# Charger le modèle sauvegardé
@st.cache(allow_output_mutation=True)
def load_model():
    return joblib.load("model.pkl")  # Sauvegarde ton modèle avec joblib avant d'exécuter ce script

# Initialisation
data = load_data()
model = load_model()

# Titre du Dashboard
st.title("Dashboard : Prédiction des Ventes")
st.write("Un outil interactif pour explorer les données et prédire les ventes.")

# Section 1 : Visualisation des données
st.header("1. Exploration des Données")
st.write("Voici un aperçu des données disponibles :")
st.dataframe(data.head())

# Visualisation des ventes par magasin
st.write("Visualisation des ventes par magasin :")
store_sales = data.groupby("store_nbr")["sales"].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(store_sales['store_nbr'], store_sales['sales'], color='skyblue')
ax.set_title("Total des Ventes par Magasin")
ax.set_xlabel("Numéro du Magasin")
ax.set_ylabel("Total des Ventes")
st.pyplot(fig)

# Section 2 : Simuler des Prédictions
st.header("2. Simulation de Prédictions")
st.write("Entrez les paramètres pour prédire les ventes :")

# Champs pour les caractéristiques d'entrée
store_nbr = st.selectbox("Numéro du Magasin", sorted(data['store_nbr'].unique()))
year = st.selectbox("Année", sorted(data['date'].dt.year.unique()))
month = st.slider("Mois", 1, 12, 1)
day = st.slider("Jour", 1, 31, 1)
day_of_week = st.selectbox("Jour de la Semaine (0=Lundi, 6=Dimanche)", list(range(7)))

# Créer l'entrée utilisateur sous forme de DataFrame
user_input = pd.DataFrame({
    'store_nbr': [store_nbr],
    'year': [year],
    'month': [month],
    'day': [day],
    'day_of_week': [day_of_week]
})

st.write("Données d'entrée :")
st.dataframe(user_input)

# Prédiction
if st.button("Prédire les Ventes"):
    # Normalisation ou transformation des données (si nécessaire)
    scaler = MinMaxScaler()
    user_input_scaled = scaler.fit_transform(user_input)
    
    # Faire la prédiction
    prediction = model.predict(user_input)
    
    st.write(f"Prédiction des Ventes : **{prediction[0]:.2f}** unités")

# Section 3 : Résultats globaux
st.header("3. Résultats Globaux")
st.write("Comparaison des prédictions et des ventes réelles.")
