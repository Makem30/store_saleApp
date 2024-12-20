import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np
import plotly.express as px

# import matplotlib.pyplot as plt
# import seaborn as sns

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

