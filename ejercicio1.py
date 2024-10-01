import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Custom CSS for background, text color, and layout
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFCCCB; /* Light pink background */
    }
    h1, h2, h3, p {
        color: #333333; /* Darker text for better contrast */
    }
    .container {
        display: flex;
        justify-content: space-between;
    }
    .left-side {
        width: 50%;
    }
    .right-side {
        width: 40%;
        background-color: white;
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #ddd;
    }
    .right-side p {
        margin: 5px 0;
        font-size: 16px;
    }
    .stSlider {
        background-color: #FFFFFF; /* Background color for slider */
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Parámetros
memoria = 1024  
eficiencia_re = 0.8  

# Función para calcular los datos procesados
def datos_procesados(n, x):
    if n <= 5:
        return n * x
    else:
        return 5 * x + (n - 5) * eficiencia_re * x

# Mostrar el gráfico primero
st.markdown('<div class="container">', unsafe_allow_html=True)

# Lado izquierdo: Gráfico
st.markdown('<div class="left-side">', unsafe_allow_html=True)
max_lotes_input = st.slider('SELECCIONA NUMERO DE LOTES', 1, 10, 8)
lotes = np.arange(1, max_lotes_input + 1)
datos = np.array([datos_procesados(n, memoria / n) for n in lotes])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(lotes, datos, marker='o', linestyle='-', color='b', label='Datos procesados')
ax.set_title('DATOS PROCESADOS Y NUMERO DE LOTES', fontsize=16, fontweight='bold')
ax.set_xlabel('Número de lotes', fontsize=12)
ax.set_ylabel('Datos procesados (MB)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(fontsize=10)
st.pyplot(fig)
st.markdown('</div>', unsafe_allow_html=True)

# Lado derecho: Resultados en un cuadro ordenado
st.markdown('<div class="right-side">', unsafe_allow_html=True)

# Mostrar los resultados: máximo, mínimo y valores en cada punto
max_dato = np.max(datos)
min_dato = np.min(datos)

st.markdown(f"**Máximo de datos procesados**: {max_dato:.2f} MB")
st.markdown(f"**Mínimo de datos procesados**: {min_dato:.2f} MB")
st.markdown("**Datos procesados en cada punto**:")
for n, dato in zip(lotes, datos):
    st.markdown(f"Número de lotes: {n}, Datos procesados: {dato:.2f} MB")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
