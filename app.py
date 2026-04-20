import streamlit as st
import pandas as pd
from datetime import datetime

# --- BASE DE DATOS ---
# Se eliminó la línea duplicada que causaba el SyntaxError
productos = {
    "13002": {"desc": "Control remoto Motorola DCT700 y STB P2.7 (sin pilas)", "precio": 28.29},
    "13004": {"desc": "Control remoto Cisco PDS-2140 y Cisco PDS-2144 (sin pilas)", "precio": 70.90},
    "13005": {"desc": "Control remoto Sagemcom DCIWI303 HD", "precio": 30.18},
    "13008": {"desc": "CONTROL REMOTO PARA DECO SAGEMCOM COD 13008", "precio": 10220.69},
    "13009": {"desc": "CONTROL REMOTO PARA DECO MOTOROLA COD 13009", "precio": 1508.00},
    "13010": {"desc": "CONTROL POR VOZ", "precio": 1508.00},
    "30032": {"desc": "Cable Coaxil RG6 Quadshield Negro con portante", "precio": 208.17},
    "30033": {"desc": "Cable Coaxil RG6 Quadshield Blanco sin portante", "precio": 208.00},
    "30035": {"desc": "Cable Coaxil RG11 Quadshield con portante", "precio": 412.39},
    "30062": {"desc": "CABLE DROP 1F0 80M. UN EXTREMO PRECONECTORIZADO SC/APC.", "precio": 18272.04},
    "31007": {"desc": "Tirafondo 8 mm x 75mm (5/16 x 2 61/64). Cabeza hexagonal", "precio": 1.65},
    "31025": {"desc": "Precinto Plastico Negro (150 x 5.5 mm) UV", "precio": 8.40},
    "31026": {"desc": "Tarugo de 8mm", "precio": 11.46},
    "31027": {"desc": "Piton con tope para Tarugo de 8mm", "precio": 47.15},
    "31028": {"desc": "Torniquete zincado N°5", "precio": 16.36},
    "31051": {"desc": "Linga 3,20 mm", "precio": 1.64},
    "31091": {"desc": "Grampa Fratacho", "precio": 10.51},
    "31096": {"desc": "Piton cerrado con tope para tarugo de 6mm", "precio": 1.90},
    "31097": {"desc": "Tarugo de 6mm", "precio": 1.50},
    "31153": {"desc": "Morseto FO", "precio": 1205.37},
    "31154": {"desc": "Etiqueta de identificacion para drop fo", "precio": 87.06},
    "32046": {"desc": "Cerrojo de dos pernos para caja estanca", "precio": 176.63},
    "32050": {"desc": "Cable tipo sintenax 2x1,5", "precio": 14.78},
    "32084": {"desc": "Soporte Pasivo (L)", "precio": 300.00},
    "32085": {"desc": "Pasapared blanco para RG6", "precio": 8.57},
    "32099": {"desc": "Siloc transparente cart. 90g y 100g", "precio": 180.00},
    "32119": {"desc": "CAJA ROCKER 10 X 10", "precio": 700.00},
    "33005": {"desc": "Grampa media omega de chapa zincada de 3/8", "precio": 0.63},
    "33006": {"desc": "Tornillo parker de 3.9 mm x 31,75 mm", "precio": 0.25},
    "33043": {"desc": "Gancho C p/torniqueta", "precio": 7.75},
    "33061": {"desc": "Caja estanca chica edificio 65x45x15cm", "precio": 509.00},
    "33067": {"desc": "Caja estanca chica para edificio con tapa", "precio": 1766.29},
    "33072": {"desc": "Clavo blanco para interior 75 mm (Grampa)", "precio": 0.25},
    "35042": {"desc": "Precinto S20 azul FO 2 vias", "precio": 12.36},
    "45139": {"desc": "PATCHCORD SC/APC - SC/APC 2MTS MONOMODO", "precio": 300.00},
    "45176": {"desc": "PATCHCORD SC/APC SC/APC MONOMODO DE 1,5 M", "precio": 300.00},
    "48170": {"desc": "PATCHCORD LC/UPC - SC/APC. 8 M / 3 MM MONOMODO", "precio": 1191.00},
    "50002": {"desc": "Decodificador Motorola DCT700 Full Digital (Recuperado)", "precio": 3442.62},
    "50004": {"desc": "Decodificador Telecentro STB P2.7 (Recuperado)", "precio": 2458.73},
    "50005": {"desc": "Decodificador HD Motorola DCX700 HD (Recuperado)", "precio": 5792.42},
    "50006": {"desc": "Fuente deco HD DCX700 Output 5V 3A", "precio": 226.32},
    "50007": {"desc": "Decodificador HD DVR Motorola DCX3400 (Recuperado)", "precio": 17146.22},
    "50008": {"desc": "Decodificador HD Cisco PDS-2140 DVB MPEG-4 (Recuperado)", "precio": 9000.00},
    "50009": {"desc": "Decodificador HD DVR Cisco PDS-2144 DVB MPEG-4 (Recuperado)", "precio": 17146.22},
    "50012": {"desc": "Decodificador HD Sagemcom DCIW303 HD (Recuperado)", "precio": 185000.00},
    "50013": {"desc": "Decodificador HD Sagemcom DCIW386 4k", "precio": 185000.00},
    "50014": {"desc": "Decodificador HD Sagemcom DCIW362 4k", "precio": 185000.00},
    "50015": {"desc": "VIDEO SOUND BOX SAGEMCOM 3930", "precio": 185000.00},
    "50016": {"desc": "DECODIFICADOR 4K SAGEMCOM DIW377", "precio": 185000.00},
    "50017": {"desc": "Decodificador HD Sagemcom DCIW362 4k AMARILLA", "precio": 185000.00},
    "50018": {"desc": "DECODIFICADOR 4K SEI ROBOTICS SEI800", "precio": 185000.00},
    "51001": {"desc": "Modem Motorola SBV5120i (Recuperado)", "precio": 7100.00},
    "51019": {"desc": "Modem Scientific Atlanta DPC2203 (Recuperado)", "precio": 1563.69},
    "51023": {"desc": "Modem SA DPC2420 WiFi (Recuperado)", "precio": 5905.38},
    "51025": {"desc": "Modem SA DPC2420 2 ptos WiFi (Recuperado)", "precio": 5905.38},
    "51026": {"desc": "Modem Cisco DPC 3925 WiFi (Recuperado)", "precio": 6100.00},
    "51030": {"desc": "Modem Arris TM501A MTA (Recuperado)", "precio": 2070.84},
    "51031": {"desc": "Modem Technicolor TC7110 AR (Recuperado)", "precio": 5925.00},
    "51033": {"desc": "Router TpLink WR841N 300Mbps", "precio": 1300.00},
    "51035": {"desc": "Modem Cisco DPC 3928 WiFi", "precio": 15000.00},
    "51036": {"desc": "MODEM SAGEMCOM F@ST 3284 WiFi", "precio": 185000.00},
    "51039": {"desc": "Modem Sagemcom F@ST 3486 WiFi (Recupero)", "precio": 185000.00},
    "51040": {"desc": "Modem Sagemcom F@ST 3686 WiFi", "precio": 185000.00},
    "51047": {"desc": "Modem Sagemcom F@ST 3686v2 WiFi (Recuperado)", "precio": 185000.00},
    "51050": {"desc": "Modem Sagemcom F@ST 3890 WiFi Docsis 3.1", "precio": 185000.00},
    "51053": {"desc": "XPON ZTE CPE ZXHN F260A", "precio": 185000.00},
    "51058": {"desc": "GPON HUAWEI ONT HG8247Q", "precio": 185000.00},
    "51060": {"desc": "MODEM 3.1 SAGEMCOM F@ST 3896 V3", "precio": 185000.00},
    "51065": {"desc": "MODEM 3.1 SAGEMCOM F@ST 3896", "precio": 185000.00},
    "51066": {"desc": "GPON SAGEMCOM F@ST 5670 PON 11X", "precio": 185000.00},
    "51069": {"desc": "MODEM 3.1 SAGEMCOM F@ST 3896", "precio": 185000.00},
    "51300": {"desc": "MESH", "precio": 88240.00},

    # --- FUENTES DE ALIMENTACIÓN ---
    "50038": {"desc": "Fuente Rukus Indoor FSA15H (12v 1.25a)", "precio": 217.48},
    "50050": {"desc": "FUENTE DECO DIGITAL", "precio": 217.48},
    "51004": {"desc": "Fuente para modem Arris TM501A", "precio": 153.62},
    "51013": {"desc": "Fuente para modem SA DPX2203", "precio": 169.74},
    "51020": {"desc": "Fuente para modem SA DPC2203", "precio": 94.35},
    "51024": {"desc": "Fuente para modem Cisco/Motorola/Technicolor", "precio": 202.21},
    "51027": {"desc": "Fuente para modem Cisco DPC 3925/8", "precio": 86.52},
    "51029": {"desc": "Fuente para modem Technicolor/Thomson DWG874", "precio": 86.52},
    "51032": {"desc": "Fuente para modem Technicolor TC7110", "precio": 86.52},
    "51037": {"desc": "Fuente para modem Sagemcom F@ST 3284", "precio": 151.98},
    "51041": {"desc": "Fuente para modem Sagemcom F@st 3486/3686", "precio": 181.99},
    "51043": {"desc": "Fuente para AP Indoor R710", "precio": 79.54},
    "51044": {"desc": "Fuente para deco Sagemcom DCIW303 HD", "precio": 3393.01},
    "51048": {"desc": "Fuente para AP Indoor C500", "precio": 196.14},
    "51051": {"desc": "Fuente para modem Sagemcom F@st 3890", "precio": 5629.96},
    "51054": {"desc": "Fuente 12V-2A GPON / Arris / SA", "precio": 151.98},
    "51055": {"desc": "Fuente 12V 3A XPON ZTE", "precio": 151.98},
    "51063": {"desc": "Fuente 12V 2A GPON HUAWEI", "precio": 151.98},
    "51067": {"desc": "Fuente 12V-2.5A Sagemcom Fast 5670", "precio": 4137.43},

    # --- CABLES Y ACCESORIOS ---
    "51018": {"desc": "INTERLOCK - CABLE DE ALIMENTACIÓN DE 220V", "precio": 16.36},
    "60069": {"desc": "Cinta aisladora plástica negra 20mts", "precio": 190.00},
    "70016": {"desc": "Cable de Red UTP (Patchcord Ethernet)", "precio": 972.04},
    "70017": {"desc": "CABLE AUDIO Y VIDEO ESTEREO RCA", "precio": 145.00},
    "70098": {"desc": "Cable HDMI", "precio": 378.01},
    "70220": {"desc": "Cable RCA a plug 3.5", "precio": 572.42},
    "87022": {"desc": "Zapatilla tomacorriente con interruptor", "precio": 57.96},
    "87029": {"desc": "Ficha 220V 10A Macho", "precio": 48.57},
    "87030": {"desc": "Ficha 220V 10A Hembra", "precio": 48.57},

    # --- PASIVOS Y FILTROS ---
    "85036": {"desc": "EQ. EDB (1GHZ)", "precio": 350.36},
    "85038": {"desc": "EQ. 6DB (1GHZ)", "precio": 350.36},
    "85054": {"desc": "GAINMAKER INVERSE EQUALIZER 9.8 DB", "precio": 29.88},
    "85056": {"desc": "GAINMAKER INVERSE EQUALIZER 13DB", "precio": 116.78},
    "85058": {"desc": "GAINMAKER INVERSE EQUALIZER 16.2DB", "precio": 116.78},
    "85265": {"desc": "SURGE-GAP REV WNDW FP TAP 8WAY", "precio": 1002.00},
    "87031": {"desc": "Divisor de 3 bocas desbalanceado", "precio": 920.10},
    "90001": {"desc": "Filtro Pasa Altos de 54-860Mhz", "precio": 40.81},
    "90090": {"desc": "Divisor de 2 bocas - Splitter x2", "precio": 635.50},
    "90091": {"desc": "Divisor de 4 bocas - Splitter x4", "precio": 1063.23},
    "90092": {"desc": "Divisor de 8 bocas - Splitter x8", "precio": 1100.00},
    "90105": {"desc": "Filtro Pasa Altos de 85Mhz", "precio": 46.08},

    # --- COMPONENTES DE INSTALACIÓN ---
    "87003": {"desc": "Conector de compresión para RG11", "precio": 1231.26},
    "87025": {"desc": "Conector de Compresión para RG6", "precio": 162.00},
    "87026": {"desc": "O-ring para conectores RG6", "precio": 23.74},
    "90005": {"desc": "Adaptador Din Macho - F Hembra", "precio": 0.96},
    "90012": {"desc": "TRANSICION MACHO-MACHO DE 5/8 (KS-KS)", "precio": 73.91},
    "90024": {"desc": "Transicion 5/8 a F sin bloqueo", "precio": 33.19},
    "90035": {"desc": "Carga de 75 Ohm para conector F", "precio": 3.99},
    "90040": {"desc": "Adaptador F hembra a DIN Grueso Macho", "precio": 0.83},
    "90047": {"desc": "Antirobo cilindrico", "precio": 6.60},
    "90071": {"desc": "Cinta Autovulcanizante", "precio": 1010.38},
    "90072": {"desc": "Grampa negra con clavo para interior", "precio": 18.13},
    "90093": {"desc": "Tubo Union (Hembra-Hembra)", "precio": 20.00},
    "90109": {"desc": "Grampa FO", "precio": 25.22},

    # --- ATENUADORES Y COUPLERS ---
    "90053": {"desc": "Atenuador domiciliario de 6dB", "precio": 150.00},
    "90054": {"desc": "Atenuador domiciliario de 10dB", "precio": 150.00},
    "90055": {"desc": "Atenuador domiciliario de 12dB", "precio": 150.00},
    "90057": {"desc": "Atenuador domiciliario de 8dB", "precio": 150.00},
    "90058": {"desc": "Atenuador domiciliario de 3dB", "precio": 150.00},
    "90059": {"desc": "Atenuador domiciliario de 20dB", "precio": 150.00},
    "90060": {"desc": "Coupler domiciliario de 6dB", "precio": 430.00},
    "90061": {"desc": "Coupler domiciliario de 9dB", "precio": 430.00},
    "90062": {"desc": "Coupler domiciliario de 12dB", "precio": 430.00},
    "90064": {"desc": "Coupler domiciliario de 20dB", "precio": 430.00},
    "90069": {"desc": "Atenuador domiciliario de 16dB", "precio": 150.00},
    "ALAR30": {"desc": "ALARGUE 30 MTS", "precio": 25000.00},
    "BANDE": {"desc": "BANDERA", "precio": 3500.00},
    "BOLHEI": {"desc": "BOLSO EINHELL", "precio": 30000.00},
    "BUTUE": {"desc": "BULON DEL 8 + TUERCA", "precio": 200.00},
    "CINTA20": {"desc": "PASACABLE 20 MTS ALMA DE ACERO", "precio": 6500.00},
    "COAMARRE": {"desc": "COLA DE AMARRE", "precio": 40000.00},
    "DETECT": {"desc": "DETECTOR DE TENSION DIGITAL", "precio": 1612.00},
    "ESCOPALA": {"desc": "ESCOBA + PALA", "precio": 1500.00},
    "FIBRON": {"desc": "FIBRON", "precio": 120.00},
    "FUNDA-CEL": {"desc": "FUNDA PARA CELULAR", "precio": 2000.00},
    "LAPIZSCL": {"desc": "LAPIZ LIMPIADOR ONE CLICK SC", "precio": 4678.00},
    "LATAEN": {"desc": "LATA ENDUIDO 1 LITRO", "precio": 1128.00},
    "MESH": {"desc": "Extensor Wifi AIRTIES AIR4960X", "precio": 35000.00},
    "MOTOE7P": {"desc": "CELULAR MOTO E7 PLUS", "precio": 50000.00},
    "N0600": {"desc": "PISTOLA CARTUCHO SILICONA", "precio": 7500.00},
    "NT0066": {"desc": "DESTORNILLADOR BUSCA POLO DIGITAL SICA", "precio": 281.00},
    "NT0067": {"desc": "PORTA HERRAMIENTAS 6 BOLSILLOS ROTTWELLER", "precio": 599.00},
    "NT0101": {"desc": "CRIMPEADORA RG6 RG11 COMPRESION", "precio": 28000.00},
    "NT0102": {"desc": "PELA CABLE COAXIAL", "precio": 15000.00},
    "NT0103": {"desc": "SACATRAMPAS", "precio": 24000.00},
    "NT0136": {"desc": "LLAVE COMBINADA DE 3/4", "precio": 1200.00},
    "NT0139": {"desc": "LLAVE T DE 10", "precio": 800.00},
    "NT0142": {"desc": "LLAVE T DE 1/2", "precio": 600.00},
    "NT0143": {"desc": "LLAVE T DE 11", "precio": 700.00},
    "NT0144": {"desc": "ROTULADORA", "precio": 7000.00},
    "NT0145": {"desc": "TESTER RJ45", "precio": 4957.00},
    "NT0147": {"desc": "GUANTES DIELECTRICOS", "precio": 6738.00},
    "NT0150": {"desc": "TELEFONO DE PRUEBA", "precio": 1000.00},
    "NT0154": {"desc": "CASCO DE SEGURIDAD", "precio": 6500.00},
    "NT0155": {"desc": "CINTURON CON CABO DE VIDA", "precio": 45000.00},
    "NT0160": {"desc": "MECHA DE ACERO 10MM", "precio": 600.00},
    "NT0163": {"desc": "MECHA DE VIDIA 6MM", "precio": 600.00},
    "NT0164": {"desc": "MECHA DE VIDIA 8MM", "precio": 5000.00},
    "NT0165": {"desc": "MECHA DE VIDIA 10MM", "precio": 900.00},
    "NT0170": {"desc": "MECHA DE 10MM PASANTE", "precio": 12469.00},
    "NT0171": {"desc": "MECHA DE 8MM CON ENCASTRE", "precio": 600.00},
    "NT0173": {"desc": "MECHA DE 10MM CON ENCASTRE", "precio": 700.00},
    "NT0176": {"desc": "PINZA DE PUNTA", "precio": 5420.00},
    "NT0177": {"desc": "PINZA DE FUERZA", "precio": 1392.70},
    "NT0179": {"desc": "DESTORNILLADOR PLANO 6X100MM", "precio": 3600.00},
    "NT0180": {"desc": "BUSCA POLO", "precio": 114.42},
    "NT0181": {"desc": "DESTORNILLADOR PHILLIP", "precio": 3600.00},
    "NT0182": {"desc": "CUTTER", "precio": 4200.00},
    "NT0183": {"desc": "CRIMPEADORA RJ45", "precio": 6478.00},
    "NT0184": {"desc": "ALICATE DE 6", "precio": 9500.00},
    "NT0185": {"desc": "MARTILLO", "precio": 8000.00},
    "NT0186": {"desc": "LLAVE FRANCESA DE 8", "precio": 899.00},
    "NT0187": {"desc": "LLAVE F O CAMPANA", "precio": 682.80},
    "NT0189": {"desc": "PINZA UNIVERSAL", "precio": 12017.00},
    "NT0190": {"desc": "GUANTE MOTEADO", "precio": 55.61},
    "NT0191": {"desc": "AGUJEREADORA", "precio": 9530.00},
    "NT0192": {"desc": "LLAVES DE EDIFICIO (PAR)", "precio": 60.00},
    "NT0197": {"desc": "TALADRO PERCUTOR DE WALT", "precio": 180000.00},
    "NT0198": {"desc": "MECHA DE 10MM PASANTE CON ENCASTRE", "precio": 700.00},
    "NT0202": {"desc": "CINTA PASACABLE 15MTS", "precio": 8732.00},
    "NT0204": {"desc": "LLAVE COMBINADA DE 7/16", "precio": 6500.00},
    "NT0205": {"desc": "MECHA DE ACERO 8MM", "precio": 868.00},
    "NT0206": {"desc": "ORGANIZADOR PLASTICO", "precio": 200.00},
    "NT0207": {"desc": "CONO", "precio": 6397.00},
    "NT0208": {"desc": "MORRAL CON CINTURON", "precio": 650.00},
    "NT0209": {"desc": "ESCALERA DIELECTRICA PARA POSTE", "precio": 450000.00},
    "NT0210": {"desc": "LLAVE COMBINADA DE 11", "precio": 1100.00},
    "NT0213": {"desc": "ALICATE 8 STANLEY", "precio": 9500.00},
    "NT0217": {"desc": "ESCALERA DIELECTRICA 10 + 10", "precio": 450000.00},
    "NT0218": {"desc": "ESCALERA DIELECTRICA PARA POSTE SERIADA", "precio": 578000.00},
    "NT0224": {"desc": "LAPIZ OPTICO", "precio": 25000.00},
    "NT0226": {"desc": "CRIMPEADORA BNC", "precio": 1300.00},
    "NT0231": {"desc": "ANTEOJOS DE SEGURIDAD", "precio": 3500.00},
    "NT0234": {"desc": "MECHA DE 12MM PASANTE CON ENCASTRE", "precio": 1200.00},
    "NT0239": {"desc": "LLAVE T DE 8", "precio": 800.00},
    "NT0244": {"desc": "DESTORNILLADOR PLANO 6X150MM", "precio": 500.00},
    "NT0251": {"desc": "DESTORNILLADOR PHILLIP PERILLERO", "precio": 899.00},
    "NT0252": {"desc": "DESTORNILLADOR PLANO PERILLERO", "precio": 899.00},
    "NT0254": {"desc": "ARNES 3 ARGOLLAS", "precio": 70000.00},
    "NT0300": {"desc": "CLEAVER FIBRA OPTICA", "precio": 55000.00},
    "NT0301": {"desc": "PELA CABLE FIBRA OPTICA (STRIPPER)", "precio": 9200.00},
    "NT032": {"desc": "NOTEBOOK LENOVO B50-80", "precio": 55000.00},
    "NT0320": {"desc": "MECHA DE 6MM CON ENCASTRE", "precio": 600.00},
    "NT0322": {"desc": "TIJERA PARA KEVLAR FO", "precio": 7500.00},
    "NT0323": {"desc": "ROTOPERCUTORA DEWALT", "precio": 25000.00},
    "NT0354": {"desc": "LLAVE FRANCESA DE 10", "precio": 2200.00},
    "NT0355": {"desc": "LLAVE FRANCESA DE 12", "precio": 3000.00},
    "NT0356": {"desc": "LLAVE COMBINADA DE 3/4", "precio": 600.00},
    "NT0357": {"desc": "LLAVE COMBINADA DE 19", "precio": 1300.00},
    "NT0358": {"desc": "LLAVE COMBINADA DE 29", "precio": 2800.00},
    "NT0400": {"desc": "CADENA PARA ESCALERA", "precio": 15000.00},
    "NT0405": {"desc": "ALARGUE 10 MTS", "precio": 17000.00},
    "NT0410": {"desc": "BATERIA 9 VOLTS", "precio": 898.00},
    "NT0413": {"desc": "CABLE ADAPTADOR USB A SERIAL RS232 DB9", "precio": 3000.00},
    "NT0432": {"desc": "CABLE DE CONSOLA", "precio": 2000.00},
    "NT0482": {"desc": "ESPATULA PINTOR N 48", "precio": 891.00},
    "NT0495": {"desc": "ESCUADRA DE ALBAÑIL", "precio": 230.52},
    "NT0496": {"desc": "PLOMADA DE ALBAÑIL", "precio": 165.85},
    "NT05": {"desc": "BOLSO PORTA HERRAMIENTAS STANLEY", "precio": 68700.00},
    "NT0521": {"desc": "PELA BUFFER", "precio": 9800.00},
    "NT0530": {"desc": "OTDR EXFO AX-S110", "precio": 194700.00},
    "NT0550": {"desc": "POW METER 54DB", "precio": 27500.00},
    "NT0551": {"desc": "PELACABLE PROSKIT", "precio": 22500.00},
    "NT0574": {"desc": "SELLO PERSONAL", "precio": 480.00},
    "NT0581": {"desc": "TALADRO DAEWOO DAID850C", "precio": 150000.00},
    "NT0585": {"desc": "CANDADO INTERSTAL", "precio": 25000.00},
    "NT0588": {"desc": "CARGADOR DE CELULAR", "precio": 5000.00},
    "NT0592": {"desc": "ROCIADOR", "precio": 746.00},
    "NT0593": {"desc": "MICROTELEFONO", "precio": 4000.00},
    "NT0594": {"desc": "PAÑOS DE LIMPIEZA", "precio": 1.54},
    "NT0599": {"desc": "ESCALERA CHICA 4 ESCALONES DE ALUMINIO", "precio": 50000.00},
    "NT0602": {"desc": "PATCHCORD SC APC PRUEBA", "precio": 1500.00},
    "NT0608": {"desc": "ANTIPARRA PARA PROTECCION OCULAR", "precio": 600.00},
    "NT11": {"desc": "LLAVE FRANCESA DE 6", "precio": 900.00},
    "NT321": {"desc": "BOLSO PORTA KIT DE FO", "precio": 14600.00},
    "NT322": {"desc": "TIJERA PARA KEVLAR FO", "precio": 2772.00},
    "NT401": {"desc": "ALCOHOL ISOPROPILICO", "precio": 2000.00},
    "PILAA": {"desc": "PILA AA", "precio": 300.00},
    "PROTEC-CEL": {"desc": "PROTECTOR HYDROGEL", "precio": 2000.00},
    "SAMA22": {"desc": "CELULAR SAMSUNG A22", "precio": 150000.00},
    "SIM": {"desc": "SIM CORPORATIVA", "precio": 600.00},
    "TALBOSH": {"desc": "TALADRO PERCUTOR BOSCH", "precio": 150000.00},
    "TALUMI": {"desc": "TALADRO PERCUTOR UMI 550W", "precio": 70000.00}
}

st.set_page_config(page_title="Auditoría de Stock", layout="wide")

if 'carrito' not in st.session_state:
    st.session_state.carrito = []
if 'ver_recibo' not in st.session_state:
    st.session_state.ver_recibo = False

st.title("📊 Auditoría de Stock")

# --- CARGA DE DATOS ---
with st.expander("➕ Cargar Nuevo Artículo", expanded=not st.session_state.ver_recibo):
    col1, col2, col3 = st.columns([2, 1, 1])
    codigo = col1.text_input("Código del Artículo:").strip()
    cantidad = col2.number_input("Cantidad:", min_value=1, value=1)
    
    if col3.button("Añadir a Planilla", use_container_width=True):
        if codigo in productos:
            nuevo_item = {
                "Código": codigo,
                "Descripción": productos[codigo]["desc"],
                "Cantidad": cantidad,
                "Precio Unit.": productos[codigo]["precio"],
                "Subtotal": productos[codigo]["precio"] * cantidad
            }
            st.session_state.carrito.append(nuevo_item)
            st.session_state.ver_recibo = False
            st.rerun()
        else:
            st.error("Código inexistente")

# --- TABLA DE EDICIÓN ---
if st.session_state.carrito:
    df = pd.DataFrame(st.session_state.carrito)
    
    st.subheader("📝 Planilla de Faltantes")
    st.data_editor(
        df,
        column_config={
            "Precio Unit.": st.column_config.NumberColumn(format="$ %.2f"),
            "Subtotal": st.column_config.NumberColumn(format="$ %.2f"),
        },
        disabled=["Código", "Descripción", "Precio Unit.", "Subtotal"],
        hide_index=True,
        use_container_width=True,
        key="editor"
    )

    total_final = df["Subtotal"].sum()

    # --- BOTONES DE ACCIÓN ---
    st.divider()
    c1, c2, c3 = st.columns(3)
    
    if c1.button("🗑️ Limpiar Todo"):
        st.session_state.carrito = []
        st.session_state.ver_recibo = False
        st.rerun()

    csv = df.to_csv(index=False).encode('utf-8-sig')
    c2.download_button("💾 Exportar CSV", csv, "auditoria.csv", "text/csv", use_container_width=True)

    if c3.button("🚀 Vista Previa para Imprimir", use_container_width=True):
        st.session_state.ver_recibo = True

    # --- VISTA PREVIA SENCILLA PARA IMPRIMIR ---
    if st.session_state.ver_recibo:
        st.divider()
        
        # Título y Fecha
        st.header("NOTIFICACIÓN DE AUDITORÍA")
        col_fecha1, col_fecha2 = st.columns([3, 1])
        col_fecha2.write(f"**Fecha:** {datetime.now().strftime('%d/%m/%Y')}")
        
        st.write(f"Me dirijo a usted desde el área de Stock a los fines de informarle y entregarle el resultado de auditoria sobre sus equipos, materiales y herramientas que fueron entregados en el establecimiento. El mismo ha arrojado faltantes por un valor de **${total_final:,.2f}**, el cual será descontado de su liquidación final.")
        
        # Mostramos la tabla limpia (Ordenada: Código, Descripción, Cantidad, Subtotal)
        # Reordenamos las columnas para que queden como pediste
        df_imprimir = df[["Código", "Descripción", "Cantidad", "Subtotal"]]
        
        # st.table genera una tabla estática, blanca y perfecta para imprimir
        st.table(df_imprimir.style.format({"Subtotal": "${:,.2f}"}))
        
        # Total al final
        st.markdown(f"<h3 style='text-align: right;'>TOTAL A CARGO: ${total_final:,.2f}</h3>", unsafe_allow_html=True)
        
        # Espacio para firma
        st.write("\n" * 4) # Espacio en blanco
        st.markdown("""
            <div style="text-align: center;">
                <p>__________________________________________</p>
                <p><b>FIRMA DEL RESPONSABLE</b></p>
            </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 Para imprimir: Haz clic derecho en cualquier parte blanca -> Imprimir (o Ctrl+P)")

        if st.button("❌ Cerrar Vista Previa"):
            st.session_state.ver_recibo = False
            st.rerun()
else:
    st.info("Ingrese un código de producto para comenzar la planilla.")
