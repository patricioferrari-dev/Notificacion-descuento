import streamlit as st

# Base de datos (resumida para el ejemplo, asegurate de completar los que falten)
productos = # --- BASE DE DATOS COMPLETA ---
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
    "31025": {"desc": "Precinto Plástico Negro (150 x 5.5 mm) , con protección U.V.", "precio": 8.41},
    "31026": {"desc": "Tarugo de 8mm", "precio": 11.46},
    "31027": {"desc": "Piton con tope para Tarugo de 8mm", "precio": 47.16},
    "31028": {"desc": "Torniquete zincado N°5", "precio": 16.36},
    "31051": {"desc": "Linga 3,20 mm", "precio": 1.64},
    "31091": {"desc": "Grampa Fratacho", "precio": 10.51},
    "31096": {"desc": "Piton cerrado con tope, para tarugo de 6mm", "precio": 1.9},
    "31097": {"desc": "Tarugo de 6mm", "precio": 1.5},
    "31153": {"desc": "Morseto FO", "precio": 1205.37},
    "31154": {"desc": "Etiqueta de identificacion para drop fo", "precio": 87.06},
    "32001": {"desc": "Nomenclador N° 1", "precio": 1.96},
    "32002": {"desc": "Nomenclador N° 2", "precio": 1.96},
    "32003": {"desc": "Nomenclador N° 3", "precio": 1.96},
    "32004": {"desc": "Nomenclador N° 4", "precio": 1.96},
    "32005": {"desc": "Nomenclador N° 5", "precio": 1.96},
    "32006": {"desc": "Nomenclador N° 6", "precio": 1.96},
    "32007": {"desc": "Nomenclador N° 7", "precio": 1.96},
    "32008": {"desc": "Nomenclador N° 8", "precio": 1.96},
    "32009": {"desc": "Nomenclador N° 9", "precio": 1.96},
    "32010": {"desc": "Nomenclador N° 0", "precio": 1.96},
    "32011": {"desc": "Nomenclador letra A", "precio": 1.96},
    "32012": {"desc": "Nomenclador letra B", "precio": 1.96},
    "32013": {"desc": "Nomenclador letra C", "precio": 1.96},
    "32014": {"desc": "Nomenclador letra D", "precio": 1.96},
    "32015": {"desc": "Nomenclador letra E", "precio": 1.96},
    "32016": {"desc": "Nomenclador letra F", "precio": 1.96},
    "32017": {"desc": "Nomenclador letra G", "precio": 1.96},
    "32018": {"desc": "Nomenclador letra H", "precio": 1.96},
    "32019": {"desc": "Nomenclador letra I", "precio": 1.96},
    "32020": {"desc": "Nomenclador letra J", "precio": 1.96},
    "32021": {"desc": "Nomenclador letra K", "precio": 1.96},
    "32022": {"desc": "Nomenclador letra L", "precio": 1.96},
    "32023": {"desc": "Nomenclador letra P", "precio": 1.96},
    "32024": {"desc": "Nomenclador letra Y", "precio": 1.96},
    "32025": {"desc": "Nomenclador letra N", "precio": 1.96},
    "32026": {"desc": "Nomenclador letra Q", "precio": 1.96},
    "32027": {"desc": "Nomenclador letra R", "precio": 1.96},
    "32028": {"desc": "Nomenclador letra W", "precio": 1.96},
    "32029": {"desc": "Nomenclador letra X", "precio": 1.96},
    "32030": {"desc": "Nomenclador letra T", "precio": 1.96},
    "32031": {"desc": "Nomenclador letra Z", "precio": 1.96},
    "32032": {"desc": "Nomenclador letra U", "precio": 1.96},
    "32033": {"desc": "Nomenclador letra V", "precio": 1.96},
    "32034": {"desc": "Nomenclador letra O", "precio": 1.96},
    "32035": {"desc": "Nomenclador letra M", "precio": 1.96},
    "32036": {"desc": "Nomenclador letra S", "precio": 1.96},
    "32046": {"desc": "Cerrojo de dos pernos para caja estanca", "precio": 176.63},
    "32050": {"desc": "Cable tipo sintenax 2x1,5", "precio": 14.78},
    "32084": {"desc": "Soporte Pasivo (L)", "precio": 300.00},
    "32085": {"desc": "Pasapared blanco para RG6", "precio": 8.57},
    "32099": {"desc": "Siloc transparente cart. 90g y 100g", "precio": 180.00},
    "32119": {"desc": "CAJA ROCKER 10 X 10", "precio": 700.00},
    "33005": {"desc": "Grampa media omega de chapa zincada de 3/8\"", "precio": 0.63},
    "33006": {"desc": "Tornillo parker de 3.9 mm x 31,75 mm", "precio": 0.25},
    "33043": {"desc": "Gancho 'C' p/torniqueta", "precio": 7.75},
    "33061": {"desc": "Caja estanca chica para edificio, 65x45x15cm", "precio": 509.00},
    "33067": {"desc": "Caja estanca chica para edificio con tapa", "precio": 1766.29},
    "33072": {"desc": "Clavo blanco para interior 75 mm (Grampa)", "precio": 0.25},
    "35042": {"desc": "Precinto S20 azul FO 2 vias", "precio": 12.37},
    "45139": {"desc": "PATCHCORD SC/APC - SC/APC 2MTS MONOMODO", "precio": 300.00},
    "45176": {"desc": "PATCHCORD SC/APC SC/APC MONOMODO DE 1,5 M", "precio": 300.00},
    "48170": {"desc": "PATCHCORD LC/UPC - SC/APC. 8 M", "precio": 1191.00},
    "50002": {"desc": "Decodificador Motorola DCT700 Full Digital (Recuperado)", "precio": 3442.62},
    "50004": {"desc": "Decodificador Telecentro STB P2.7 (Recuperado)", "precio": 2458.73},
    "50005": {"desc": "Decodificador HD Motorola DCX700 HD (Recuperado)", "precio": 5792.42},
    "50006": {"desc": "Fuente deco HD DCX700. 5V 3A", "precio": 226.32},
    "50007": {"desc": "Decodificador HD DVR Motorola DCX3400 (Recuperado)", "precio": 17146.22},
    "50008": {"desc": "Decodificador HD Cisco PDS-2140 (Recuperado)", "precio": 9000.00},
    "50009": {"desc": "Decodificador HD DVR Cisco PDS-2144 (Recuperado)", "precio": 17146.22},
    "50012": {"desc": "Decodificador HD Sagemcom DCIW303 HD (Recuperado)", "precio": 185000.00},
    "50013": {"desc": "Decodificador HD Sagemcom DCIW386 4k", "precio": 185000.00},
    "50014": {"desc": "Decodificador HD Sagemcom DCIW362 4k", "precio": 185000.00},
    "50015": {"desc": "VIDEO SOUND BOX SAGEMCOM 3930", "precio": 185000.00},
    "50016": {"desc": "DECODIFICADOR 4K SAGEMCOM DIW377", "precio": 185000.00},
    "50017": {"desc": "Decodificador HD Sagemcom DCIW362 4k ETIQUETA AMARILLA", "precio": 185000.00},
    "50018": {"desc": "DECODIFICADOR 4K SEI ROBOTICS SEI800", "precio": 185000.00},
    "50038": {"desc": "Fuente de alimentacion para Rukus Indoor. 12v 1.25a", "precio": 217.48},
    "50050": {"desc": "FUENTE DECO DIGITAL", "precio": 217.48},
    "51001": {"desc": "Modem Motorola SBV5120i (Recuperado)", "precio": 7100.00},
    "51004": {"desc": "Fuente para modem Arris TM501A", "precio": 153.62},
    "51013": {"desc": "Fuente para modem Scientific Atlanta DPX2203", "precio": 169.74},
    "51018": {"desc": "INTERLOCK - CABLE DE ALIMENTACIÓN DE 220V", "precio": 16.36},
    "51019": {"desc": "Modem Scientific Atlanta DPC2203 con MTA (Recuperado)", "precio": 1563.69},
    "51020": {"desc": "Fuente para modem Scientific Atlanta DPC2203", "precio": 94.30},
    "51023": {"desc": "Modem Scientific Atlanta DPC2420 WiFi (Recuperado)", "precio": 5905.38},
    "51024": {"desc": "Fuente para modem Cisco/Motorola/Technicolor", "precio": 202.21},
    "51025": {"desc": "Modem Scientific Atlanta DPC2420 WiFi 2 ptos (Recuperado)", "precio": 5905.38},
    "51026": {"desc": "Modem Cisco DPC 3925 WI-FI (recuperado)", "precio": 6100.00},
    "51027": {"desc": "Fuente para modem Cisco DPC 3925/8 WI-FI", "precio": 86.52},
    "51029": {"desc": "Fuente para modem Technicolor/Thomson DWG874", "precio": 86.52},
    "51030": {"desc": "Modem Arris TM501A (Recuperado)", "precio": 2070.84},
    "51031": {"desc": "Modem Technicolor TC7110 AR (Recuperado)", "precio": 5925.00},
    "51032": {"desc": "Fuente para modem Technicolor TC7110", "precio": 86.52},
    "51033": {"desc": "Router TpLink - WR841N 300Mbps Wireless N", "precio": 1300.00},
    "51035": {"desc": "Modem Cisco DPC 3928 WI-FI 4 ptos red", "precio": 15000.00},
    "51036": {"desc": "MODEM SAGEMCOM F@ST 3284 WI-FI", "precio": 185000.00},
    "51037": {"desc": "Fuente para modem Sagemcom F@ST 3284", "precio": 151.98},
    "51039": {"desc": "Modem Sagemcom F@ST 3486 WI-FI (recupero)", "precio": 185000.00},
    "51040": {"desc": "Modem Sagemcom F@ST 3686 WI-FI", "precio": 185000.00},
    "51041": {"desc": "Fuente para modem Sagemcom F@st 3486/3686", "precio": 181.99},
    "51043": {"desc": "Fuente para access point indoor R710", "precio": 79.54},
    "51044": {"desc": "Fuente para deco Sagemcom DCIW303 HD", "precio": 3393.02},
    "51047": {"desc": "Modem Sagemcom F@ST 3686v2 WI-FI (recuperado)", "precio": 185000.00},
    "51048": {"desc": "Fuente para access point indoor C500", "precio": 196.14},
    "51050": {"desc": "Modem Sagemcom F@ST 3890 WI-FI Docsis 3.1", "precio": 185000.00},
    "51051": {"desc": "Fuente para modem Sagemcom F@st 3890", "precio": 5629.97},
    "51053": {"desc": "XPON ZTE CPE ZXHN F260A", "precio": 185000.00},
    "51054": {"desc": "FUENTE ALIMENTACION 12V-2A", "precio": 151.98},
    "51055": {"desc": "FUENTE ALIMENTACION 12V 3A XPON", "precio": 151.98},
    "51058": {"desc": "GPON HUAWEI ONT HG8247Q", "precio": 185000.00},
    "51059": {"desc": "Caja FO", "precio": 788.60},
    "51060": {"desc": "MODEM 3.1 SAGEMCOM F@ST 3896 V3", "precio": 185000.00},
    "51063": {"desc": "FUENTE ALIMENTACIONN 12V 2A GPON HUAWEI", "precio": 151.98},
    "51065": {"desc": "MODEM 3.1 SAGEMCOM F@ST 3896", "precio": 185000.00},
    "51066": {"desc": "GPON SAGEMCOM F@ST 5670 PON 11X", "precio": 185000.00},
    "51067": {"desc": "FUENTE ALIMENTACION 12V-2,5A/ SAGEMCOM FAST 5670", "precio": 4137.43},
    "51069": {"desc": "MODEM 3.1 SAGEMCOM F@ST 3896", "precio": 185000.00},
    "51300": {"desc": "MESH", "precio": 88240.00},
    "60069": {"desc": "Cinta aisladora plástica color negro de 20mts.", "precio": 190.00},
    "70016": {"desc": "Cable de Red UTP para PC (Patchcord Ethernet)", "precio": 972.05},
    "70017": {"desc": "CABLE DE AUDIO Y VIDEO ESTEREO RCA", "precio": 145.00},
    "70098": {"desc": "Cable HDMI", "precio": 378.02},
    "70181": {"desc": "Access Point INDOOR - Rukus R500", "precio": 11597.75},
    "70219": {"desc": "Access point wall mounting C500", "precio": 228.39},
    "70220": {"desc": "Cable RCA a plug 3.5", "precio": 572.43},
    "70320": {"desc": "RUCKUS C110", "precio": 15037.99},
    "85036": {"desc": "4007230 EQ. EDB (1GHZ)", "precio": 350.36},
    "85038": {"desc": "4007232 EQ. 6DB (1GHZ)", "precio": 350.36},
    "85054": {"desc": "4007491 GAINMAKER INVERSE EQUALIZER 1GHZ 9,8 DB", "precio": 29.88},
    "85056": {"desc": "4007493 GAINMAKER INVERSE EQUALIZER 1GHZ 13DB", "precio": 116.78},
    "85058": {"desc": "4007495 GAINMAKER INVERSE EQUALIZER 1GHZ 16,2DB", "precio": 116.78},
    "85265": {"desc": "SG-RW-8-F26R20-FP TAP 1.25GHZ", "precio": 1002.00},
    "85278": {"desc": "SG-TAP-8-17-FP TAP 1.25GHZ", "precio": 1002.00},
    "86011": {"desc": "Pads Plug-in de 1dB para Gain Maker", "precio": 29.88},
    "86012": {"desc": "Pads Plug-in de 2dB para Gain Maker", "precio": 29.88},
    "86013": {"desc": "Pads Plug-in de 3dB para Gain Maker", "precio": 29.88},
    "86014": {"desc": "Pads Plug-in de 4dB para Gain Maker", "precio": 29.88},
    "86016": {"desc": "Pads Plug-in de 6dB para Gain Maker", "precio": 29.88},
    "86017": {"desc": "PADS PLUG-IN DE 7DB PARA GAIN MAKER", "precio": 29.88},
    "86018": {"desc": "Pads Plug-in de 8dB para Gain Maker", "precio": 29.88},
    "86019": {"desc": "Pads Plug-in de 9dB para Gain Maker", "precio": 29.88},
    "86020": {"desc": "Pads Plug-in de 10dB para Gain Maker", "precio": 29.88},
    "86030": {"desc": "Pads Plug-in de 20dB para Gain Maker", "precio": 29.88},
    "87003": {"desc": "Conector de compresión para RG11", "precio": 1231.26},
    "87022": {"desc": "Zapatilla tomacorriente con interruptor", "precio": 57.96},
    "87024": {"desc": "Transicion 5/8 a F con bloqueo de tension", "precio": 363.62},
    "87025": {"desc": "Conector de Compresión para RG6", "precio": 162.00},
    "87026": {"desc": "O'ring para conectores de RG 6", "precio": 23.74},
    "87031": {"desc": "Divisor de 3 bocas desbalanceado - Splitter x3", "precio": 920.10},
    "90002": {"desc": "Pila alcalinas AAA para control remoto", "precio": 222.61},
    "90053": {"desc": "Atenuador domiciliario de 6dB", "precio": 150.00},
    "90090": {"desc": "Divisor de 2 bocas - Splitter x2", "precio": 635.50},
    "90091": {"desc": "Divisor de 4 bocas - Splitter x4", "precio": 1063.23},
    "90092": {"desc": "Divisor de 8 bocas - Splitter x8", "precio": 1100.00},
    "92015": {"desc": "Amplificador de edificio Compact Mini 36 db - 220 V", "precio": 1981.22},
    "92041": {"desc": "Amplificador de edificio CISCO GS LE", "precio": 2492.54},
    "1017703": {"desc": "CONECTOR RJ45 MACHO CAT.5E", "precio": 12.00},
    "1017704": {"desc": "CONTROL_REMOTO IPTV", "precio": 416.00},
    "1018991": {"desc": "FUENTE 12 VDC-1 AMP", "precio": 1100.00},
    "1019716": {"desc": "CONECTOR MECANICO SM SC-APC 3MM", "precio": 590.00},
    "1021441": {"desc": "Preconectorizado DROP fig8 100 m", "precio": 2560.00},
    "1022698": {"desc": "Preconectorizado DROP fig8 50 m", "precio": 1570.00},
    "1022699": {"desc": "GPON-KIT de instalacion 20M", "precio": 2700.00},
    "1025894": {"desc": "PRECO ROUND CABLE E&F 70 MTS", "precio": 4100.00},
    "1025955": {"desc": "PRECO ROUND CABLE E&F 130 MTS", "precio": 9231.00},
    "1026648": {"desc": "PRECO ROUND CABLE E&F (VD) 180 MTS", "precio": 14100.00},
    "4014506": {"desc": "HUAWEI GPON H68245H", "precio": 11405.00},
    "4014518": {"desc": "DECO STB KAON SC7210", "precio": 8500.00},
    "ALAR30": {"desc": "ALARGUE 30 MTS", "precio": 25000.00},
    "MESH": {"desc": "Extensor Wifi AIRTIES AIR4960X", "precio": 35000.00},
    "NT0197": {"desc": "TALADRO PERCUTOR DE WALT", "precio": 180000.00},
    "NT0209": {"desc": "ESCALERA DIELECTRICA PARA POSTE", "precio": 450000.00},
    "NT0218": {"desc": "ESCALERA DIELECTRICA PARA POSTE SERIADA", "precio": 578000.00},
    "NT0300": {"desc": "CLEAVER FIBRA OPTICA", "precio": 55000.00},
    "NT0530": {"desc": "OTDR EXFO AX-S110", "precio": 194700.00},
    "SAMA22": {"desc": "CELULAR SAMSUNG A22", "precio": 150000.00},
    "TALBOSHT": {"desc": "TALADRO PERCUTOR BOSCH", "precio": 150000.00},
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
