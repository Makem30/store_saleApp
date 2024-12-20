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
# selected_year = st.sidebar.selectbox("Sélectionner l'année", train['date'].dt.year.unique())
# selected_month = st.sidebar.selectbox("Sélectionner le mois", train['date'].dt.month.unique())

# Filtrer les données en fonction des sélections
# import streamlit as st
# import pandas as pd 
# import altair as alt
# import numpy as np
# chart = alt.Chart(filtered_data).mark_bar().encode(
#        alt.X("sales:Q", bin=True),
#        alt.Y("count()")
#    ).properties(
#        title=f"Distribution des ventes pour {selected_month}/{selected_year}"
#    )
# st.altair_chart(chart, use_container_width=True)



# Grouper les données par mois et calculer les ventes totales
monthly_sales = train.groupby(train['date'].dt.to_period('M'))['sales'].sum().reset_index()
monthly_sales['date'] = monthly_sales['date'].dt.to_timestamp()  # Revenir à un format de date

# Créer le graphique avec Plotly Express
fig = px.bar(monthly_sales, x='date', y='sales', title="Ventes totales par mois")
fig.update_xaxes(title_text="Mois")
fig.update_yaxes(title_text="Ventes totales")

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)
