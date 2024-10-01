import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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
        background-color: #FFFFFF; /* Color del slider */
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Función para calcular ancho de banda
def calcular_ancho_banda(archivos_transmitidos, ancho_banda_total=1000):
    if archivos_transmitidos > 30:
        archivos_extra = archivos_transmitidos - 30
        reduccion = (5 / 100) * archivos_extra
        ancho_banda_disponible = ancho_banda_total * (1 - reduccion)
    else:
        ancho_banda_disponible = ancho_banda_total
    return max(0, ancho_banda_disponible)

# Función para maximizar archivos
def maximizar_archivos(x, ancho_banda_total=1000):
    for archivos in range(50, 0, -1):  
        ancho_banda_disponible = calcular_ancho_banda(archivos, ancho_banda_total)
        if archivos * x <= ancho_banda_disponible:  
            return archivos, ancho_banda_disponible
    return 0, 0

# Título de la aplicación
st.title("Maximización de Transmisión de Archivos con Gráfico")

# Sliders para ancho de banda por archivo y total
x = st.slider("Ancho de banda por archivo (Mbps)", min_value=1, max_value=100, value=20)
ancho_banda_total = st.slider("Ancho de banda total del sistema (Mbps)", min_value=500, max_value=2000, value=1000)

# Botón para realizar el cálculo
if st.button("Calcular Máximo de Archivos"):
    archivos_max, ancho_banda_restante = maximizar_archivos(x, ancho_banda_total)
    
    # Layout de la presentación en dos columnas
    st.markdown('<div class="container">', unsafe_allow_html=True)

    # Lado izquierdo: Resultados
    st.markdown('<div class="right-side">', unsafe_allow_html=True)
    
    st.write(f"**Número máximo de archivos que se pueden transmitir:** {archivos_max}")
    st.write(f"**Ancho de banda disponible restante:** {ancho_banda_restante:.2f} Mbps")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Lado derecho: Gráfico
    st.markdown('<div class="left-side">', unsafe_allow_html=True)
    
    archivos = np.arange(1, 51)
    ancho_banda_disponible = [calcular_ancho_banda(a, ancho_banda_total) for a in archivos]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(archivos, ancho_banda_disponible, label='Ancho de banda disponible (Mbps)', color='b')
    ax.axvline(x=30, color='red', linestyle='--', label='Límite sin penalización')
    ax.axvline(x=archivos_max, color='green', linestyle='--', label=f'Máximo Archivos: {archivos_max}')
    ax.set_xlabel('Número de archivos transmitidos', fontsize=12)
    ax.set_ylabel('Ancho de banda disponible (Mbps)', fontsize=12)
    ax.set_title('Relación entre número de archivos y ancho de banda disponible', fontsize=16, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(fontsize=10)
    
    st.pyplot(fig)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
