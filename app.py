import streamlit as st

# Base de datos (resumida para el ejemplo, asegurate de completar los que falten)
productos = {
    "13002": {"desc": "Control remoto para deco Motorola DCT700", "precio": 28.29},
    "13008": {"desc": "CONTROL REMOTO PARA DECO SAGEMCOM COD 13008", "precio": 10220.69},
    "1025962": {"desc": "Retención para Round cable con gancho", "precio": 123.00},
    "NT0197": {"desc": "TALADRO PERCUTOR DE WALT", "precio": 180000.00},
    "NT0209": {"desc": "ESCALERA DIELECTRICA PARA POSTE", "precio": 450000.00},
    "MESH": {"desc": "Extensor Wifi AIRTIES AIR4960X", "precio": 35000.00},
    # Agregá aquí el resto de tu lista...
}

st.set_page_config(page_title="Sistema de Carga de Artículos", layout="wide")

# Inicializar el "carrito" o lista de carga si no existe
if 'lista_carga' not in st.session_state:
    st.session_state.lista_carga = []

st.title("📋 Gestión de Artículos y Resumen")

# --- SECCIÓN DE CARGA ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Cargar Artículo")
    codigo_input = st.text_input("Código del Artículo:").strip()
    
    if st.button("➕ Agregar a la lista"):
        if codigo_input in productos:
            # Agregamos el producto a la memoria de la sesión
            st.session_state.lista_carga.append(productos[codigo_input])
            st.success(f"Agregado: {productos[codigo_input]['desc']}")
        else:
            st.error("Código no encontrado.")

# --- SECCIÓN DE RESUMEN ---
st.divider()
st.subheader("📝 Resumen de Carga")

if st.session_state.lista_carga:
    # Mostrar tabla de lo cargado
    total_final = 0
    for i, item in enumerate(st.session_state.lista_carga):
        col_a, col_b, col_c = st.columns([4, 1, 0.5])
        col_a.write(f"**{item['desc']}**")
        col_b.write(f"${item['precio']:,.2f}")
        total_final += item['precio']
        
        # Botón opcional para borrar un ítem
        if col_c.button("❌", key=f"btn_{i}"):
            st.session_state.lista_carga.pop(i)
            st.rerun()

    st.divider()
    st.markdown(f"### TOTAL A PROCESAR: **${total_final:,.2f}**")

    # --- PROCESAR FINAL (Notificación) ---
    if st.button("🚀 Generar Notificación Final"):
        # Armamos el texto para la "hoja" final
        texto_resumen = "RESUMEN DE CARGA DE ARTÍCULOS\n"
        texto_resumen += "="*40 + "\n"
        for item in st.session_state.lista_carga:
            texto_resumen += f"- {item['desc']}: ${item['precio']:,.2f}\n"
        texto_resumen += "="*40 + "\n"
        texto_resumen += f"TOTAL: ${total_final:,.2f}\n"
        texto_resumen += "\nNotificación generada automáticamente."

        st.text_area("Notificación Final para copiar/imprimir:", texto_resumen, height=300)
        
        st.download_button(
            label="Descargar Informe TXT",
            data=texto_resumen,
            file_name="resumen_carga.txt",
            mime="text/plain"
        )
else:
    st.info("La lista está vacía. Ingresá un código a la izquierda para empezar.")

# Botón para limpiar todo
if st.sidebar.button("🗑️ Vaciar Lista Completa"):
    st.session_state.lista_carga = []
    st.rerun()
