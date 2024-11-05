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

# Estadísticas básicas del DataFrame
st.subheader("Estadísticas descriptivas")
st.write(df.describe())



# Graficar la duración de las canciones
st.subheader("Duración de las canciones")
plt.figure(figsize=(10, 6))
sns.histplot(df["duration"] / 1000, kde=True, color='green')  # Convertir a segundos
plt.title("Distribución de Duración de las Canciones (segundos)")
plt.xlabel("Duración (segundos)")
plt.ylabel("Frecuencia")
st.pyplot()



# Filtro interactivo para el usuario
st.sidebar.header("Filtros")
selected_genre = st.sidebar.selectbox("Selecciona un género", options=df['genre'].unique())
filtered_data = df[df['genre'] == selected_genre]

st.subheader(f"Canciones del género: {selected_genre}")
st.write(filtered_data[['track_name', 'artist', 'popularity', 'duration_ms']])
