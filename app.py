import streamlit as st

# 1. Base de datos de productos (Simulada)
# Podés cambiar esto por un archivo CSV más adelante
productos = {
    "ART001": {"nombre": "Remera Algodón", "precio": 15000},
    "ART002": {"nombre": "Pantalón Jean", "precio": 45000},
    "ART003": {"nombre": "Zapatillas Runner", "precio": 85000},
}

# Configuración de la página
st.set_page_config(page_title="Generador de Descuentos", page_icon="🏷️")

st.title("🏷️ Sistema de Notificación de Descuentos")
st.markdown("Ingresá el código del artículo para generar la etiqueta de oferta.")

# 2. Entrada de datos
codigo = st.text_input("Código del Artículo:", placeholder="Ej: ART001").upper()
descuento = st.number_input("Porcentaje de descuento (%):", min_value=0, max_value=100, value=10)

if codigo:
    if codigo in productos:
        prod = productos[codigo]
        precio_original = prod['precio']
        ahorro = precio_original * (descuento / 100)
        precio_final = precio_original - ahorro

        # 3. El texto de tu notificación
        texto_notificacion = f"""
        **********************************************
        ¡OFERTA ESPECIAL!
        
        Artículo: {prod['nombre']}
        Precio Regular: ${precio_original:,.2f}
        DESCUENTO APLICADO: {descuento}%
        
        PRECIO FINAL: ${precio_final:,.2f}
        ----------------------------------------------
        Presentá este código en caja: DISC-{codigo}
        **********************************************
        """

        # Mostrar en pantalla
        st.success("¡Código encontrado!")
        st.text_area("Previsualización de la Notificación:", texto_notificacion, height=250)

        # 4. Botón para "Imprimir" (Simulado mediante descarga de TXT)
        st.download_button(
            label="Descargar Notificación para Imprimir",
            data=texto_notificacion,
            file_name=f"descuento_{codigo}.txt",
            mime="text/plain"
        )
    else:
        st.error("El código de artículo no existe en la base de datos.")

# Footer informativo
st.sidebar.info("Para actualizar precios, editá el diccionario en el código fuente.")
