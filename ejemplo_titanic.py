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

# Graficar la distribución de la popularidad de las canciones
st.subheader("Distribución de Popularidad")
plt.figure(figsize=(10, 6))
sns.histplot(df['popularity'], kde=True, color='blue')
plt.title("Distribución de Popularidad de las Canciones")
plt.xlabel("Popularidad")
plt.ylabel("Frecuencia")
st.pyplot()

# Graficar la duración de las canciones
st.subheader("Duración de las canciones")
plt.figure(figsize=(10, 6))
sns.histplot(df['duration_ms'] / 1000, kde=True, color='green')  # Convertir a segundos
plt.title("Distribución de Duración de las Canciones (segundos)")
plt.xlabel("Duración (segundos)")
plt.ylabel("Frecuencia")
st.pyplot()

# Graficar el número de canciones por género
st.subheader("Número de Canciones por Género")
genre_count = df['genre'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=genre_count.index, y=genre_count.values, palette='viridis')
plt.title("Número de Canciones por Género")
plt.xlabel("Género")
plt.ylabel("Número de Canciones")
plt.xticks(rotation=45)
st.pyplot()

# Filtro interactivo para el usuario
st.sidebar.header("Filtros")
selected_genre = st.sidebar.selectbox("Selecciona un género", options=df['genre'].unique())
filtered_data = df[df['genre'] == selected_genre]

st.subheader(f"Canciones del género: {selected_genre}")
st.write(filtered_data[['track_name', 'artist', 'popularity', 'duration_ms']])
