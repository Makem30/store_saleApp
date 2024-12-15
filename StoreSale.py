import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np

#Charger les Données :
holidays_events = pd.read_csv('holidays_events.csv', delimiter=",")
train = pd.read_csv('train.csv', delimiter=",")
test = pd.read_csv('test.csv', delimiter=",")
stores = pd.read_csv('stores.csv', delimiter=",")
oil = pd.read_csv('oil.csv', delimiter=",")
sample_submission = pd.read_csv('sample_submission.csv', delimiter=",")
transactions = pd.read_csv('transactions.csv', delimiter=",")

# Create two columns
# col1, col2 = st.columns([0.5,0.4],gap="large")

# with col1:

  #Content for the first column
# with col2:

with st.sidebar:
  st.title('DASHBOARD')
  st.sidebar.title("Comparateur de données")
