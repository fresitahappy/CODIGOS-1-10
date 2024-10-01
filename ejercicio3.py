import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Custom CSS for background, text color, and layout
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFCCCB; /* Fondo rosado claro */
    }
    h1, h2, h3, p {
        color: #333333; /* Texto más oscuro para mejor contraste */
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
        background-color: #FFFFFF; /* Color de fondo del slider */
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Título y subtítulo
st.title('Tiempo de ejecución del script vs Número de datos procesados')
st.write('')

# Slider para límite de tiempo
limite_tiempo = st.slider('Límite máximo de tiempo (segundos)', 10, 100, 50) 

# Función para calcular el tiempo de ejecución
def tiempo_ejecucion(x):
    return 5 * x + 2

# Valores en el eje x
x_val = np.arange(0, 11)  
tiempos = tiempo_ejecucion(x_val)

# Layout de la presentación en dos columnas
st.markdown('<div class="container">', unsafe_allow_html=True)

# Lado izquierdo: Gráfico
st.markdown('<div class="left-side">', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x_val, tiempos, label='Tiempo de ejecución', color='b', marker='o')
ax.axhline(limite_tiempo, color='r', linestyle='--', label=f'Límite de {limite_tiempo} segundos')
ax.set_title('Tiempo de ejecución del script vs Número de datos procesados', fontsize=16, fontweight='bold')
ax.set_xlabel('Número de datos procesados', fontsize=12)
ax.set_ylabel('Tiempo de ejecución (segundos)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(fontsize=10)
st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)

# Lado derecho: Mostrar resultados
st.markdown('<div class="right-side">', unsafe_allow_html=True)

# Mostrar el límite de tiempo
st.markdown(f"**Límite máximo de tiempo seleccionado**: {limite_tiempo} segundos")

# Mostrar los tiempos de ejecución para cada punto
for x in x_val:
    st.markdown(f"**Número de datos procesados**: {x}, **Tiempo de ejecución**: {tiempo_ejecucion(x)} segundos")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
