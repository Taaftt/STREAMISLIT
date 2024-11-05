import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV "database_titanic.csv" en un DataFrame de pandas.
df = pd.read_csv("top 100 streamed_songs.csv")

#Titulo
st.title("Mejores 100 canciones de spotify")
#descripcion
st.write("Explora los mejores temas")

st.subheader("Primeras filas de los datos")
st.write(df.head())
