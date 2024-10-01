import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Custom CSS para mejorar la presentación
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFCCCB; /* Fondo rosado claro */
    }
    h1, h2, h3, p {
        color: #333333; /* Color oscuro del texto */
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
    </style>
    """, unsafe_allow_html=True
)

# Título de la aplicación
st.title('Latencia vs Número de Mensajes')

# Slider para seleccionar el número de mensajes por segundo
numero_mensajes = st.slider(
    'Selecciona el número de mensajes por segundo',
    min_value=0,
    max_value=60,
    value=0  
)

# Función para calcular la latencia
def latencia(x):
    return 100 - 2 * x

# Parámetros y valores calculados
x_val = np.linspace(0, 60, 100)
latencias = latencia(x_val)
x_max = 40  # Valor máximo de mensajes sin penalización
latencia_seleccionada = latencia(numero_mensajes)

# Layout en dos columnas para presentación
st.markdown('<div class="container">', unsafe_allow_html=True)

# Lado izquierdo: Gráfico
st.markdown('<div class="left-side">', unsafe_allow_html=True)

# Creación del gráfico
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_val, latencias, label='Latencia (ms)', color='b')
ax.axhline(y=20, color='r', linestyle='--', label='Latencia mínima de 20 ms')
ax.axvline(x=x_max, color='g', linestyle='--', label=f'Máximo mensajes: {x_max}')
ax.plot(numero_mensajes, latencia_seleccionada, 'go', label=f'Seleccionado: {numero_mensajes} mensajes')

# Anotaciones y detalles en el gráfico
ax.text(x_max + 1, 20 + 5, f'Máximo mensajes: {x_max}', color='green', fontsize=10)
ax.text(numero_mensajes + 1, latencia_seleccionada + 5, f'{latencia_seleccionada:.2f} ms', color='purple', fontsize=10)

# Personalización del gráfico
ax.set_title('Latencia vs Número de Mensajes', fontsize=16, fontweight='bold')
ax.set_xlabel('Número de mensajes por segundo', fontsize=12)
ax.set_ylabel('Latencia (ms)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(fontsize=10)
st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)

# Lado derecho: Información adicional
st.markdown('<div class="right-side">', unsafe_allow_html=True)

# Mostrar información adicional sobre la latencia y el número de mensajes
st.markdown(f"### Detalles adicionales:")
st.markdown(f"**Latencia inicial sin mensajes:** 100 ms")
st.markdown(f"**Latencia mínima permitida:** 20 ms")
st.markdown(f"**Tasa de reducción de latencia:** 2 ms por cada mensaje adicional")

# Mostrar el máximo número de mensajes que satisface la latencia mínima
st.markdown(f"**El número máximo de mensajes que mantiene la latencia mínima es:** {x_max}")

# Mostrar la latencia para el número de mensajes seleccionados
st.markdown(f"**La latencia para {numero_mensajes} mensajes por segundo es:** {latencia_seleccionada:.2f} ms")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
