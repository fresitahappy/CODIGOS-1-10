import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Custom CSS para fondo rosado claro y otros detalles estéticos
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFCCCB; /* Fondo rosado claro */
    }
    h1, h2, h3, p {
        color: #333333; /* Texto oscuro */
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
        background-color: #FFFFFF;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Título de la aplicación
st.title('Costo de Almacenamiento vs Cantidad de TB')

# Slider para seleccionar la cantidad de almacenamiento
cantidad_almacenamiento = st.slider(
    'Selecciona la cantidad de almacenamiento (TB)',
    min_value=0,
    max_value=100,
    value=0
)

# Función para calcular el costo de almacenamiento
def costo_almacenamiento(x):
    return 50 + 5 * x

# Parámetros y valores calculados
presupuesto = 500
x_val = np.linspace(0, 100, 100)
costos = costo_almacenamiento(x_val)
x_max = (presupuesto - 50) / 5
costo_seleccionado = costo_almacenamiento(cantidad_almacenamiento)

# Layout de presentación en dos columnas
st.markdown('<div class="container">', unsafe_allow_html=True)

# Lado izquierdo: Gráfico
st.markdown('<div class="left-side">', unsafe_allow_html=True)

# Creación del gráfico
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_val, costos, label='Costo de almacenamiento', color='b')
ax.axhline(y=presupuesto, color='r', linestyle='--', label='Presupuesto de 500 dólares')
ax.axvline(x=x_max, color='g', linestyle='--', label=f'Máximo almacenamiento: {x_max:.2f} TB')
ax.plot(cantidad_almacenamiento, costo_seleccionado, 'go', label=f'Seleccionado: {cantidad_almacenamiento} TB')

# Información adicional en el gráfico
ax.text(x_max + 1, presupuesto - 10, f'Máximo: {x_max:.2f} TB', color='g', fontsize=10)
ax.text(cantidad_almacenamiento + 1, costo_seleccionado + 10, f'{costo_seleccionado:.2f} USD', color='purple', fontsize=10)

# Estilo del gráfico
ax.set_title('Costo de Almacenamiento vs Cantidad de TB', fontsize=16, fontweight='bold')
ax.set_xlabel('Cantidad de almacenamiento (TB)', fontsize=12)
ax.set_ylabel('Costo de almacenamiento (dólares)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(fontsize=10)
st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)

# Lado derecho: Detalles adicionales
st.markdown('<div class="right-side">', unsafe_allow_html=True)

# Mostrar datos adicionales
st.markdown(f"### Detalles adicionales:")
st.markdown(f"**Presupuesto disponible:** 500 dólares")
st.markdown(f"**Costo base:** 50 dólares")
st.markdown(f"**Costo por TB adicional:** 5 dólares")

# Mostrar el tamaño de almacenamiento máximo que satisface el presupuesto
st.markdown(f"**El tamaño máximo de almacenamiento dentro del presupuesto es:** {x_max:.2f} TB")

# Mostrar el costo de almacenamiento para la cantidad seleccionada
st.markdown(f"**El costo de almacenamiento para {cantidad_almacenamiento} TB es:** {costo_seleccionado:.2f} dólares")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
