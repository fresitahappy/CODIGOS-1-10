import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Custom CSS para fondo rosado claro y otros estilos
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFCCCB; /* Fondo rosado claro */
    }
    h1, h2, h3, p {
        color: #333333; /* Texto en gris oscuro */
    }
    .container {
        display: flex;
        justify-content: space-between;
    }
    .left-side {
        width: 60%;
    }
    .right-side {
        width: 35%;
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #ddd;
    }
    .stSlider {
        background-color: #FFFFFF; /* Fondo del slider */
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Título de la aplicación
st.title('Consumo Total de Energía vs Tamaño de Lote')

# Slider para seleccionar el tamaño del lote
tamaño_lote = st.slider('Selecciona el tamaño del lote (x)', min_value=1, max_value=20, value=10)

# Función para calcular la energía consumida
def energia_consumida(x):
    if x <= 10:
        return x
    else:
        return x * (1 + 0.1 * (x - 10))

# Función para calcular el consumo total
def consumo_total(x):
    return x * energia_consumida(x)

# Cálculo del consumo total y valores máximos
x_values = np.linspace(1, 20, 100)
consumo = np.array([consumo_total(x) for x in x_values])
x_max = np.max(x_values[consumo <= 200])

# Layout en dos columnas
st.markdown('<div class="container">', unsafe_allow_html=True)

# Lado izquierdo: Gráfico
st.markdown('<div class="left-side">', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_values, consumo, label='Consumo total de energía', color='b')
ax.axhline(y=200, color='r', linestyle='--', label='Restricción de 200 unidades de energía')
ax.axvline(x=x_max, color='g', linestyle='--', label=f'Máximo en x={x_max:.2f}')
ax.plot(x_max, consumo_total(x_max), 'go', label=f'Punto máximo: ({x_max:.2f}, {consumo_total(x_max):.2f})')
ax.axvline(x=tamaño_lote, color='purple', linestyle='--', label=f'Tamaño de lote seleccionado: {tamaño_lote}')
ax.plot(tamaño_lote, consumo_total(tamaño_lote), 'mo', label=f'Punto seleccionado: ({tamaño_lote}, {consumo_total(tamaño_lote):.2f})')

ax.set_title('Consumo total de energía vs Tamaño de lote', fontsize=16, fontweight='bold')
ax.set_xlabel('Tamaño de lote (x)', fontsize=12)
ax.set_ylabel('Consumo total de energía (unidades)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(fontsize=10)
st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)

# Lado derecho: Detalles adicionales
st.markdown('<div class="right-side">', unsafe_allow_html=True)

# Mostrar el tamaño de lote máximo que satisface la restricción
st.markdown(f"**El tamaño de lote máximo que satisface la restricción de 200 unidades de energía es aproximadamente:** {x_max:.2f}")

# Mostrar el consumo total de energía para el tamaño de lote seleccionado
st.markdown(f"**Consumo total de energía para el tamaño de lote seleccionado ({tamaño_lote}):** {consumo_total(tamaño_lote):.2f} unidades")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
