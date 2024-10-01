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
st.title('Latencia vs Número de Mensajes')
st.write('')

# Función para calcular la latencia
def latencia(x):
    return 100 - 2 * x

# Valores en el eje x
x_val = np.linspace(0, 60, 100)
latencias = latencia(x_val)
x_max = 40  # Punto máximo

# Slider para seleccionar el número de mensajes por segundo
numero_mensajes = st.slider(
    'Selecciona el número de mensajes por segundo',
    min_value=0,
    max_value=60,
    value=0  # Valor por defecto
)

latencia_seleccionada = latencia(numero_mensajes)

# Layout de la presentación en dos columnas
st.markdown('<div class="container">', unsafe_allow_html=True)

# Lado izquierdo: Gráfico
st.markdown('<div class="left-side">', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x_val, latencias, label='Latencia (ms)', color='b')
ax.axhline(y=20, color='r', linestyle='--', label='Latencia mínima de 20 ms')
ax.axvline(x=x_max, color='g', linestyle='--', label=f'Máximo en x={x_max}')
ax.plot(numero_mensajes, latencia_seleccionada, 'go', label='Seleccionado')
ax.set_title('Latencia vs Número de Mensajes', fontsize=16, fontweight='bold')
ax.set_xlabel('Número de mensajes por segundo', fontsize=12)
ax.set_ylabel('Latencia (ms)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(fontsize=10)
st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)

# Lado derecho: Mostrar resultados
st.markdown('<div class="right-side">', unsafe_allow_html=True)

# Mostrar el valor de la latencia seleccionada
st.markdown(f"**Número de mensajes seleccionados**: {numero_mensajes}")
st.markdown(f"**Latencia para {numero_mensajes} mensajes por segundo**: {latencia_seleccionada:.2f} ms")
st.markdown(f"**Latencia mínima**: 20 ms")
st.markdown(f"**Punto máximo en x**: {x_max} mensajes por segundo")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
