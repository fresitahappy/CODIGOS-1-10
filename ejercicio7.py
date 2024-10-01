import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Custom CSS para estilo con fondo rosado claro
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
st.title('Tiempo de respuesta vs Número de trabajos procesados')

# Slider para seleccionar el número de trabajos procesados por segundo
max_x = st.slider('Selecciona el número de trabajos procesados por segundo', 5, 20, 20)

# Función para calcular el tiempo de respuesta
def tiempo_respuesta(x):
    return (100 / x) + 2 * x

# Valores de x y tiempos de respuesta
x_val = np.arange(5, max_x, 0.1)
tiempos = tiempo_respuesta(x_val)
x_optimo = np.sqrt(50)
t_optimo = tiempo_respuesta(x_optimo)
x_minimo = x_val[0]
x_maximo = x_val[-1]
t_minimo = tiempo_respuesta(x_minimo)
t_maximo = tiempo_respuesta(x_maximo)

# Layout en dos columnas: Gráfico y detalles
st.markdown('<div class="container">', unsafe_allow_html=True)

# Lado izquierdo: Gráfico
st.markdown('<div class="left-side">', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_val, tiempos, label='Tiempo de respuesta', color='b')
ax.axvline(x_optimo, color='r', linestyle='--', label=f'Mínimo en x={x_optimo:.2f}')
ax.scatter(x_optimo, t_optimo, color='r', zorder=5, label=f'Punto mínimo ({x_optimo:.2f}, {t_optimo:.2f})')
ax.scatter(x_minimo, t_minimo, color='g', zorder=5, label=f'Punto inicial ({x_minimo}, {t_minimo:.2f})')
ax.scatter(x_maximo, t_maximo, color='m', zorder=5, label=f'Punto final ({x_maximo}, {t_maximo:.2f})')

ax.set_title('Tiempo de respuesta vs Número de trabajos procesados', fontsize=16, fontweight='bold')
ax.set_xlabel('Número de trabajos por segundo', fontsize=12)
ax.set_ylabel('Tiempo de respuesta', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(fontsize=10)
st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)

# Lado derecho: Detalles de la optimización y más datos del gráfico
st.markdown('<div class="right-side">', unsafe_allow_html=True)

# Detalles del gráfico
st.markdown(f"**Número óptimo de trabajos procesados por segundo (x óptimo):** {x_optimo:.2f}")
st.markdown(f"**Tiempo de respuesta mínimo correspondiente:** {t_optimo:.2f} segundos")

# Puntos clave del gráfico
st.markdown(f"**Punto inicial:** ({x_minimo}, {t_minimo:.2f} segundos)")
st.markdown(f"**Punto final:** ({x_maximo}, {t_maximo:.2f} segundos)")

# Valores máximo y mínimo
st.markdown(f"**Tiempo máximo:** {t_maximo:.2f} segundos en {x_maximo} trabajos por segundo")
st.markdown(f"**Tiempo mínimo:** {t_minimo:.2f} segundos en {x_minimo} trabajos por segundo")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
