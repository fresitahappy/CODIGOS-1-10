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
st.title('Tiempo de entrenamiento vs Tamaño del lote (Batch size)')
st.write('')

# Slider para tamaño del lote
batch_size = st.slider('Tamaño del lote', 16, 128, 16)

# Función para calcular el tiempo de entrenamiento
def tiempo_entrenamiento(x):
    return (1000 / x) + 0.1 * x

# Valores en el eje x
x_val = np.arange(16, 129, 1)
tiempos = tiempo_entrenamiento(x_val)
min_index = np.argmin(tiempos)
batch_size_min = x_val[min_index]
tiempo_min = tiempos[min_index]
tiempo_actual = tiempo_entrenamiento(batch_size)

# Layout de la presentación en dos columnas
st.markdown('<div class="container">', unsafe_allow_html=True)

# Lado izquierdo: Gráfico
st.markdown('<div class="left-side">', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x_val, tiempos, label='Tiempo de entrenamiento', color='b')
ax.axvline(x=batch_size_min, color='r', linestyle='--', label=f'Mínimo global en x={batch_size_min} (Tiempo: {tiempo_min:.2f})')
ax.axvline(x=batch_size, color='g', linestyle='--', label=f'Tamaño de lote seleccionado: {batch_size} (Tiempo: {tiempo_actual:.2f})')
ax.set_title('Tiempo de entrenamiento vs Tamaño del lote (Batch size)', fontsize=16, fontweight='bold')
ax.set_xlabel('Tamaño del lote (Batch size)', fontsize=12)
ax.set_ylabel('Tiempo de entrenamiento', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(fontsize=10)
st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)

# Lado derecho: Mostrar resultados
st.markdown('<div class="right-side">', unsafe_allow_html=True)

# Mostrar el tamaño de lote que minimiza el tiempo de entrenamiento
st.markdown(f"**El tamaño de lote que minimiza el tiempo de entrenamiento es:** {batch_size_min} con un tiempo de {tiempo_min:.2f} ")
# Mostrar el tiempo de entrenamiento para el tamaño de lote seleccionado
st.markdown(f"**El tiempo de entrenamiento para el tamaño de lote seleccionado ({batch_size}) es:** {tiempo_actual:.2f}")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
