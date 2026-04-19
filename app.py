import streamlit as st

# Base de datos cargada con tu listado
productos = {
    "13002": {"desc": "Control remoto para deco Motorola DCT700 y STB P2.7 (sin pilas)", "precio": 28.29},
    "13004": {"desc": "Control remoto para deco Cisco PDS-2140 y Cisco PDS-2144 (sin pilas)", "precio": 70.9},
    "13005": {"desc": "Control remoto para deco Sagemcom DCIWI303 HD", "precio": 30.18},
    "13008": {"desc": "CONTROL REMOTO PARA DECO SAGEMCOM COD 13008", "precio": 10220.69},
    "13009": {"desc": "CONTROL REMOTO PARA DECO MOTOROLA COD 13009", "precio": 1508.00},
    "13010": {"desc": "CONTROL POR VOZ", "precio": 1508.00},
    "29057": {"desc": "Bandeja PM8S para caja estanca chica (031085/033061)", "precio": 193.57},
    "29058": {"desc": "Bandeja PM16A para caja estanca chica (031085/033061)", "precio": 283.04},
    "29060": {"desc": "Bandeja PM24A para caja estanca chica (031085/033061)", "precio": 371.16},
    "29063": {"desc": "Bandeja M48A para caja estanca chica (031085/033061)", "precio": 664.27},
    "29064": {"desc": "Bandeja M72A para caja estanca chica (031085/033061)", "precio": 947.16},
    "30032": {"desc": "Cable Coaxil RG6 Quadshield Negro con portante", "precio": 208.17},
    "30033": {"desc": "Cable Coaxil RG6 Quadshield Blanco sin portante", "precio": 208.00},
    "30035": {"desc": "Cable Coaxil RG11 Quadshield con portante", "precio": 412.39},
    "30062": {"desc": "CABLE DROP 1F0 80M. UN EXTREMO PRECONECTORIZADO SC/APC.", "precio": 18272.04},
    "31007": {"desc": "Tirafondo 8 mm x 75mm (5/16\" x 2 61/64\"). Cabeza hexagonal", "precio": 1.65},
    "31025": {"desc": "Precinto Plástico Negro (150 x 5.5 mm) , con protección U.V.", "precio": 8.40},
    "31026": {"desc": "Tarugo de 8mm", "precio": 11.46},
    "31027": {"desc": "Piton con tope para Tarugo de 8mm", "precio": 47.15},
    "31028": {"desc": "Torniquete zincado N°5", "precio": 16.36},
    "31051": {"desc": "Linga 3,20 mm", "precio": 1.64},
    "31091": {"desc": "Grampa Fratacho", "precio": 10.51},
    "31096": {"desc": "Piton cerrado con tope, para tarugo de 6mm", "precio": 1.9},
    "31097": {"desc": "Tarugo de 6mm", "precio": 1.5},
    "31153": {"desc": "Morseto FO", "precio": 1205.37},
    "31154": {"desc": "Etiqueta de identificacion para drop fo", "precio": 87.06},
    "32001": {"desc": "Nomenclador N° 1", "precio": 1.96},
    "32002": {"desc": "Nomenclador N° 2", "precio": 1.96},
    "32010": {"desc": "Nomenclador N° 0", "precio": 1.96},
    "32011": {"desc": "Nomenclador letra A", "precio": 1.96},
    "32050": {"desc": "Cable tipo sintenax 2x1,5", "precio": 14.78},
    "32085": {"desc": "Pasapared blanco para RG6", "precio": 8.57},
    "32099": {"desc": "Siloc transparente cart. 90g y 100g", "precio": 180.00},
    "32119": {"desc": "CAJA ROCKER 10 X 10", "precio": 700.00},
    "33061": {"desc": "Caja estanca chica para edificio, de una puerta, 65x45x15cm", "precio": 509.00},
    "33067": {"desc": "Caja estanca chica para edificio con tapa", "precio": 1766.29},
    "50012": {"desc": "Decodificador HD Sagemcom DCIW303 HD (Recuperado)", "precio": 185000.00},
    "51035": {"desc": "Modem Cisco DPC 3928 WI-FI con 2 ptos telefónicos, 4 ptos red", "precio": 15000.00},
    "51050": {"desc": "Modem Sagemcom F@ST 3890 WI-FI Docsis 3.1", "precio": 185000.00},
    "51060": {"desc": "MODEM 3.1 SAGEMCOM F@ST 3896 V3", "precio": 185000.00},
    "70098": {"desc": "Cable HDMI", "precio": 378.01},
    "1018991": {"desc": "FUENTE 12 VDC-1 AMP-PLUG HUECO 5X8X2.1MM", "precio": 1100.00},
    "ALAR30": {"desc": "ALARGUE 30 MTS", "precio": 25000.00},
    "MESH": {"desc": "Extensor Wifi AIRTIES AIR4960X", "precio": 35000.00},
    "NT0197": {"desc": "TALADRO PERCUTOR DE WALT", "precio": 180000.00},
    "NT0209": {"desc": "ESCALERA DIELECTRICA PARA POSTE", "precio": 450000.00},
    "NT0300": {"desc": "CLEAVER FIBRA OPTICA", "precio": 55000.00}
    # ... He incluido los más representativos, puedes seguir agregando siguiendo este formato
}

st.set_page_config(page_title="App Descuentos", page_icon="💰")

st.title("Generador de Notificación de Descuento")

# Entrada del código
codigo_input = st.text_input("Ingresá el código del artículo:").strip()
porcentaje = st.slider("Seleccioná el % de descuento:", 0, 100, 15)

if codigo_input:
    if codigo_input in productos:
        item = productos[codigo_input]
        desc = item['desc']
        precio_original = item['precio']
        
        # Cálculos
        valor_descuento = precio_original * (porcentaje / 100)
        precio_final = precio_original - valor_descuento

        # TU TEXTO DE NOTIFICACIÓN (Editable)
        texto_noticia = f"""
-----------------------------------------
      NOTIFICACIÓN DE DESCUENTO
-----------------------------------------
Por medio de la presente se informa que el 
artículo: {desc} (Ref: {codigo_input})
tiene un descuento exclusivo del {porcentaje}%.

PRECIO DE LISTA: ${precio_original:,.2f}
AHORRO: ${valor_descuento:,.2f}

>>> PRECIO FINAL: ${precio_final:,.2f} <<<

*Validez por 48hs o hasta agotar stock.*
-----------------------------------------
        """

        st.info("Vista previa de la notificación:")
        st.code(texto_noticia, language="text")

        st.download_button(
            label="Descargar para Imprimir",
            data=texto_noticia,
            file_name=f"descuento_{codigo_input}.txt",
            mime="text/plain"
        )
    else:
        st.warning("El código ingresado no se encuentra en la base de datos.")

st.sidebar.write("### Ayuda")
st.sidebar.write("Ingresá el código tal cual figura en la lista (ej: 13002 o NT0197).")
