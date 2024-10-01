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
st.title('Uso de CPU vs Número de peticiones procesadas por segundo')
st.write('')

# Slider para límite de uso de CPU
limite_uso_cpu = st.slider('Límite máximo de uso de CPU (%)', 50, 100, 80)
# Slider para máximo de peticiones
max_peticiones = st.slider('Máximo de peticiones procesadas por segundo', 5, 50, 20)

# Función para calcular uso de CPU
def uso_cpu(x):
    return 2 * x**2 + 10 * x

# Valores en el eje x
x_val = np.arange(0, max_peticiones + 1, 0.1)
uso_cpu_values = uso_cpu(x_val)

# Layout de la presentación en dos columnas
st.markdown('<div class="container">', unsafe_allow_html=True)

# Lado izquierdo: Gráfico
st.markdown('<div class="left-side">', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x_val, uso_cpu_values, label='Uso de CPU', color='b')
ax.axhline(limite_uso_cpu, color='r', linestyle='--', label=f'Límite del {limite_uso_cpu}% de CPU')
ax.set_title('Uso de CPU vs Número de peticiones procesadas por segundo', fontsize=16, fontweight='bold')
ax.set_xlabel('Número de peticiones procesadas por segundo', fontsize=12)
ax.set_ylabel('Uso de CPU (%)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(fontsize=10)
st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)

# Lado derecho: Mostrar resultados
st.markdown('<div class="right-side">', unsafe_allow_html=True)

# Mostrar el límite de uso de CPU
st.markdown(f"**Límite máximo de uso de CPU seleccionado**: {limite_uso_cpu} %")

# Mostrar el máximo de peticiones procesadas por segundo
st.markdown(f"**Máximo de peticiones procesadas por segundo**: {max_peticiones}")

# Mostrar los valores del uso de CPU para cada punto
for x in np.arange(0, max_peticiones + 1):
    st.markdown(f"**Número de peticiones procesadas**: {x}, **Uso de CPU**: {uso_cpu(x):.2f} %")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
