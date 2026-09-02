import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
import base64
import random
import os
import urllib.request

# Configuración adaptable profesional para múltiples pantallas
st.set_page_config(page_title="EVIL_PHOTO // Forensic Console", page_icon="👁️‍🗨️", layout="wide")

# Inyección de CSS Avanzado: Estilo Interfaz de Radar Forense Ciberpunk
st.markdown("""
    <style>
    .main { background-color: #050505; font-family: 'Courier New', monospace; }

    /* Aprovechar el ancho disponible en PC y tablet */
    .block-container {
        max-width: 1600px !important;
        width: 100% !important;
        padding-left: 2.5rem !important;
        padding-right: 2.5rem !important;
        padding-top: 2rem !important;
    }

    section[data-testid="stMain"] > div {
        max-width: 1600px !important;
        width: 100% !important;
        margin: 0 auto !important;
    }

    /* Ajuste especial para tablet y pantallas pequeñas */
    @media (max-width: 900px) {
        .block-container {
            max-width: 100% !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
    }

    @media (max-width: 600px) {
        .block-container {
            padding-left: 0.6rem !important;
            padding-right: 0.6rem !important;
        }
    }
    .titulo-consola {
        color: #ff2222;
        text-align: center;
        text-shadow: 0 0 10px #ff2222, 0 0 20px #990000;
        font-weight: bold;
        letter-spacing: 3px;
        margin-bottom: 5px;
    }
    .panel-forense {
        background-color: #0f1115;
        border: 1px solid #1f242e;
        border-left: 4px solid #ff2222;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    canvas { max-width: 100% !important; border-radius: 2px; }

    /* El monitor principal mantiene siempre la misma proporción */
    #evilCanvas {
        width: 100% !important;
        height: auto !important;
        aspect-ratio: 16 / 9;
        object-fit: contain;
    }
    
    /* Estilo ciberpunk para el cargador de archivos */
    div[data-testid="stFileUploader"] {
        background-color: #0f1115;
        border: 1px dashed #ff2222;
        border-radius: 4px;
        padding: 10px;
    }
    div[data-testid="stFileUploader"] label {
        color: #00ff66 !important;
        font-family: 'Courier New', monospace;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-consola">👁️‍🗨️ EVIL_PHOTO // QUANTUM SCANNER</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="color:#666; text-align:center; font-size:11px; margin-bottom:20px; font-family:monospace;">STATION DIGITAL DE PERITAJE FOTOGRÁFICO V26.0 // DATABASE FORUM</h3>', unsafe_allow_html=True)
# --- PANEL DE DESCRIPCIÓN FORENSE INICIAL ---
st.markdown("""
    <div class="panel-forense" style="border-left: 4px solid #00ff66; margin-bottom: 15px;">
        <p style="color: #00ff66; font-size: 13px; font-weight: bold; margin: 0 0 8px 0; text-transform: uppercase;">[MANUAL DE INDUCCIÓN // PROTOCOLO VISUAL]</p>
        <p style="color: #ccc; font-size: 12px; margin: 0 0 10px 0; line-height: 1.5;">
            <b>EVIL_PHOTO</b> es una estación digital forense optimizada para el aislamiento, remasterización, telemetría biométrica y decodificación de anomalías ópticas incrustadas en archivos de imagen.
        </p>
    </div>
""", unsafe_allow_html=True)

# Nota de recomendación, Contador persistente y Agradecimiento de donación PayPal integrado
html_HUD_info = """
<div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 25px; font-family: 'Courier New', monospace;">
    <div style="background-color: #1a1000; border: 1px solid #ffaa00; padding: 10px; border-radius: 4px; font-size: 11px; color: #ffaa00;">
        🖥️ <b>AVISO DE INTERFAZ:</b> Se recomienda encarecidamente ejecutar esta estación digital en un <b>dispositivo de pantalla grande (PC / Laptop)</b> para desplegar la mesa de control completa de manera óptima y garantizar la mejor experiencia pericial.
    </div>
    
    <div style="display: flex; justify-content: space-between; align-items: center; background-color: #0f1115; border: 1px solid #1f242e; padding: 12px; border-radius: 4px; flex-wrap: wrap; gap: 10px;">
        <div style="font-size: 12px; color: #00ff66; font-weight: bold; letter-spacing: 1px;">
            📊 RASTREADOR DE TRÁFICO SPECTRAL: <span id="contadorVisitas" style="color: #fff; background: #220000; padding: 2px 8px; border-radius: 3px; border: 1px solid #ff2222;">...</span> ACCESOS
        </div>
        <div>
            <a href="https://www.paypal.com/ncp/payment/HAALKPRK6DT8G" target="_blank" onclick="alert('⚡ TRANSMISIÓN ENCRIPTADA PAYPAL:\\n\\n¡Te agradecemos profundamente tu valiosa contribución! Tu apoyo económico será destinado al 100% para financiar los servidores, optimizar los algoritmos de red neuronal y seguir actualizando y manteniendo esta aplicación con nuevas herramientas forenses profesionales.\\n\\nPresiona Aceptar para continuar hacia la pasarela segura.')" style="
                background: linear-gradient(135deg, #003087 0%, #0079C1 100%); color: #ffffff; font-family: Arial, sans-serif; font-size: 11px; font-weight: bold; text-decoration: none; padding: 8px 16px; border-radius: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); display: inline-block; transition: transform 0.2s;
            " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                💛 APOYAR PROYECTO
            </a>
        </div>
    </div>
</div>
<script>
    let visitas = localStorage.getItem('evil_visits_counter');
    if (!visitas) { visitas = Math.floor(Math.random() * 45) + 12; }
    visitas = parseInt(visitas) + 1; localStorage.setItem('evil_visits_counter', visitas);
    document.getElementById('contadorVisitas').innerText = visitas;
</script>
"""
st.components.v1.html(html_HUD_info, height=125, scrolling=False)

# Cargador de archivos en la pantalla principal
archivo_subido = st.file_uploader("☣️ INTRODUCIR ARCHIVO DE EVIDENCIA FOTOGRÁFICA:", type=["jpg", "jpeg", "png"], key="photo_core_uploader")
st.markdown('<div style="margin-bottom: 25px;"></div>', unsafe_allow_html=True)
# --- PANEL LATERAL DE SELECCIÓN (SIDEBAR) ---
st.sidebar.header("🎛️ PANEL DE CONTROL FOTOGRÁFICO")
st.sidebar.markdown("<p style='color:#00ff66; font-size:12px; font-weight:bold;'>🎛️ FILTROS DE LUZ INTELIGENTES</p>", unsafe_allow_html=True)

activar_brillo = st.sidebar.checkbox("☀️ Modulación de Brillo")
brillo = st.sidebar.slider("Potencia de Exposición (Brillo)", -100, 100, 0) if activar_brillo else 0

activar_contraste = st.sidebar.checkbox("🌓 Amplificación de Contraste")
contraste = st.sidebar.slider("Ganancia de Contraste Dinámico", 1.0, 3.0, 1.0, 0.1) if activar_contraste else 1.0

activar_negativo = st.sidebar.checkbox("👁️ Inversión de Espectro")
negativo = st.sidebar.slider("Fusión de Negativo (%)", 0, 100, 0) if activar_negativo else 0

activar_umbral = st.sidebar.checkbox("🏁 Umbralización Binaria")
umbral_val = st.sidebar.slider("Umbral de Densidad Absoluto", 0, 255, 127) if activar_umbral else 127

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color:#00ff66; font-size:12px; font-weight:bold;'>🔍 MATRICES FORENSES REGULABLES</p>", unsafe_allow_html=True)

activar_remaster = st.sidebar.checkbox("✨ Remasterización Espectral (IA Enhancer)")
int_remaster = st.sidebar.slider("Potencia de Enfoque y Nitidez Cuántica", 1, 50, 15) if activar_remaster else 15
activar_nocturna = st.sidebar.checkbox("🟢 Visión Nocturna (Fósforo Verde)")
int_nocturna = st.sidebar.slider("Ganancia e Intensidad Verde", 10, 100, 100) if activar_nocturna else 100
activar_termica = st.sidebar.checkbox("🔴 Visión Nocturna Térmica (Mapa de Calor)")
int_termica = st.sidebar.slider("Fusión Térmica Termográfica", 10, 100, 100) if activar_termica else 100
activar_ela = st.sidebar.checkbox("🔍 Análisis ELA (Falsificación Digital)")
int_ela = st.sidebar.slider("Amplificación de Error Digital", 5, 50, 15) if activar_ela else 15
activar_ruido = st.sidebar.checkbox("🌫️ Aislamiento de Ruido de Grano")
int_ruido = st.sidebar.slider("Rango de Suavizado de Textura", 3, 25, 9, step=2) if activar_ruido else 9
activar_gradiente = st.sidebar.checkbox("📊 Gradiente Vectorial Sobel (BGA)")
int_gradiente = st.sidebar.slider("Ganancia de Sensor Térmico", 10, 100, 50) if activar_gradiente else 50
activar_relieve = st.sidebar.checkbox("🧱 Activar Relieve Térmico (Emboss)")
int_relieve = st.sidebar.slider("Profundidad de Relieve 3D", 1, 5, 1) if activar_relieve else 1
activar_ir = st.sidebar.checkbox("🛰️ Espectrografía Infrarroja")
int_ir = st.sidebar.slider("Sensibilidad Infrarroja Opaca", 0, 255, 0) if activar_ir else 0
activar_canny = st.sidebar.checkbox("🕸️ Vectorización de Bordes Canny")
int_canny = st.sidebar.slider("Umbral de Rigidez de Bordes", 10, 200, 50) if activar_canny else 50

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color:#ff2222; font-size:12px; font-weight:bold;'>⚡ TELEMETRÍA PARANORMAL EN VIVO</p>", unsafe_allow_html=True)
activar_flir = st.sidebar.checkbox("⛈️ Escáner de Temperatura Espectral (FLIR)")
int_flir = st.sidebar.slider("Sensibilidad a Puntos Fríos", 10, 100, 80) if activar_flir else 80
activar_orbes = st.sidebar.checkbox("🌌 Detector de Orbes y Polvo Espectral")
int_orbes = st.sidebar.slider("Umbral de Captura Lumínica", 10, 255, 230) if activar_orbes else 230
activar_emf = st.sidebar.checkbox("📻 Analizador de Frecuencia Fantasma (EMF)")

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color:#00ffff; font-size:12px; font-weight:bold;'>🔬 PERITAJE DE AUTENTICIDAD DIGITAL</p>", unsafe_allow_html=True)
activar_lga = st.sidebar.checkbox("📉 Gradiente de Luminancia (Detección de Montajes)")
activar_retinex = st.sidebar.checkbox("👁️‍🗨️ Realce de Sombras Densas (CLAHE Forense)")
int_retinex = st.sidebar.slider("Ganancia de Apertura de Sombras", 1, 10, 3) if activar_retinex else 3
activar_prnu = st.sidebar.checkbox("🎚️ Uniformidad de Ruido de Sensor")

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color:#ffaa00; font-size:12px; font-weight:bold;'>🔮 OPCIONES EXTRAS FORENSES</p>", unsafe_allow_html=True)
activar_biometria = st.sidebar.checkbox("🧬 Escáner Facial por Red Neuronal (DNN IA)")
if archivo_subido is not None:
    # --- PIPELINE DE PROCESAMIENTO DE IMAGEN ORIGINAL ---
    file_bytes = np.asarray(bytearray(archivo_subido.read()), dtype=np.uint8)
    img_cv = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Copia maestra SIN efectos.
    # img_cv seguirá utilizándose para el pipeline forense/procesado.
    img_original_cv = img_cv.copy()

    h_original, w_original = img_cv.shape[:2]
    
    rostros_detectados = []
    orbes_detectados = 0
    frecuencia_ruido_base = 0.0
    biometria_fallida = False
    
    if activar_retinex:
        lab = cv2.cvtColor(img_cv, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=float(int_retinex), tileGridSize=(8, 8))
        img_cv = cv2.cvtColor(cv2.merge((clahe.apply(l), a, b)), cv2.COLOR_LAB2BGR)
        
    if activar_lga:
        log_lga = np.log1p(cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY).astype(np.float32))
        cv2.normalize(log_lga, log_lga, 0, 255, cv2.NORM_MINMAX)
        img_cv = cv2.applyColorMap(log_lga.astype(np.uint8), cv2.COLORMAP_BONE)

    if activar_prnu:
        ruido_espectro = cv2.absdiff(cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY), cv2.GaussianBlur(cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY), (5, 5), 0))
        cv2.normalize(ruido_espectro, ruido_espectro, 0, 255, cv2.NORM_MINMAX)
        img_cv = cv2.cvtColor(ruido_espectro, cv2.COLOR_GRAY2BGR)

    if activar_biometria:
        try:
            model_proto, model_weight = "deploy.prototxt", "res10_300x300_ssd_iter_140000.caffemodel"
            if not os.path.exists(model_proto): urllib.request.urlretrieve("https://githubusercontent.com", model_proto)
            if not os.path.exists(model_weight): urllib.request.urlretrieve("https://githubusercontent.com", model_weight)
            net = cv2.dnn.readNetFromCaffe(model_proto, model_weight)
            net.setInput(cv2.dnn.blobFromImage(cv2.resize(img_cv, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0)))
            detecciones = net.forward()
            estados_animo = ["ANALÍTICO // ALERTA", "NEUTRO SPECTRUM", "EMOCIÓN DETECTADA", "PÁNICO SUSPENDIDO", "FELICIDAD ESPECTRAL"]
            generos = ["MASCULINO (VECTORES)", "FEMENINO (VECTORES)"]
            for i in range(detecciones.shape[2]):
                if detecciones[0, 0, i, 2] > 0.5:
                    box = detecciones[0, 0, i, 3:7] * np.array([w_original, h_original, w_original, h_original])
                    (x1, y1, x2, y2) = box.astype("int")
                    x1, y1, x2, y2 = max(0, x1), max(0, y1), min(w_original, x2), min(h_original, y2)
                    cv2.rectangle(img_cv, (x1, y1), (x2, y2), (0, 255, 102), 3)
                    semilla_id = int((x1 * y1) % 100)
                    rostros_detectados.append({"id": len(rostros_detectados) + 1, "edad": int(max(18, min(78, (semilla_id % 38) + 19))), "genero": generos[x1 % len(generos)], "animo": estados_animo[y1 % len(generos)], "confianza": round(float(detecciones[0, 0, i, 2])*100, 1)})
        except Exception: biometria_fallida = True

    if activar_flir: img_cv = cv2.addWeighted(img_cv, 1.0 - (int_flir/100.0), cv2.applyColorMap(cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY), cv2.COLORMAP_JET), int_flir/100.0, 0)
    if activar_orbes:
        _, umb_o = cv2.threshold(cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY), int_orbes, 255, cv2.THRESH_BINARY)
        contornos, _ = cv2.findContours(umb_o, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contornos:
            (ox, oy), radio = cv2.minEnclosingCircle(c)
            centro, radio = (int(ox), int(oy)), int(radio)
            if 3 < radio < 35:
                orbes_detectados += 1
                cv2.circle(img_cv, centro, radio + 4, (0, 230, 255), 2)
                cv2.putText(img_cv, f"ORBE #{orbes_detectados}", (centro + 10, centro), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 230, 255), 1)
    if activar_emf: frecuencia_ruido_base = float(np.std(cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)))
    if activar_remaster:
        img_cv = cv2.resize(img_cv, (w_original * 2, h_original * 2), interpolation=cv2.INTER_CUBIC)
        h_original, w_original = img_cv.shape[:2]
        img_cv = cv2.filter2D(img_cv, -1, np.array([[0, -1, 0], [-1, 4 + (int_remaster / 10.0), -1], [0, -1, 0]]))

    img_cv = cv2.convertScaleAbs(img_cv, alpha=contraste, beta=brillo)
    if negativo > 0: img_cv = cv2.addWeighted(img_cv, 1 - (negativo/100), cv2.bitwise_not(img_cv), negativo/100, 0)
    if activar_umbral:
        _, t_img = cv2.threshold(cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY), umbral_val, 255, cv2.THRESH_BINARY)
        img_cv = cv2.cvtColor(t_img, cv2.COLOR_GRAY2BGR)
    if activar_nocturna:
        gris = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        img_cv = cv2.addWeighted(img_cv, 1 - (int_nocturna/100), cv2.merge([np.zeros_like(gris), cv2.convertScaleAbs(gris, alpha=1.2, beta=20), np.zeros_like(gris)]), int_nocturna/100, 0)
    if activar_ruido: img_cv = cv2.medianBlur(img_cv, int_ruido if int_ruido % 2 != 0 else int_ruido + 1)
    if activar_ela:
        _, enc = cv2.imencode('.jpg', img_cv, [cv2.IMWRITE_JPEG_QUALITY, 90])
        img_cv = cv2.absdiff(img_cv, cv2.imdecode(enc, 1)) * int_ela
    if activar_gradiente:
        gris = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        img_cv = cv2.addWeighted(img_cv, 1 - (int_gradiente/100), cv2.applyColorMap(cv2.addWeighted(cv2.convertScaleAbs(cv2.Sobel(gris, cv2.CV_16S, 1, 0, ksize=3)), 0.5, cv2.convertScaleAbs(cv2.Sobel(gris, cv2.CV_16S, 0, 1, ksize=3)), 0.5, 0), cv2.COLORMAP_HOT), int_gradiente/100, 0)
    if activar_relieve: img_cv = cv2.filter2D(img_cv, -1, np.array([[-2, -1, 0], [-1, 1, 1]]) * int_relieve) + 128
    if activar_ir: img_cv = cv2.applyColorMap(cv2.add(cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY), int_ir) if int_ir > 0 else cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY), cv2.COLORMAP_BONE)
    if activar_canny: img_cv = cv2.cvtColor(cv2.Canny(img_cv, int_canny, int_canny * 3), cv2.COLOR_GRAY2BGR)
    # Tamaño interno para generar una imagen de buena calidad.
    # El monitor visual tendrá un tamaño FIJO y no cambiará según la foto.
    ancho_web = 1200
    alto_web = int((h_original / w_original) * ancho_web)
    # ---------------------------------------------------------
    # DOS FUENTES DE IMAGEN
    # ---------------------------------------------------------
    # 1. ORIGINAL: nunca recibe los efectos del pipeline.
    # 2. PROCESADA: contiene todos los filtros/efectos activos.
    img_original_render = cv2.resize(
        img_original_cv,
        (ancho_web, alto_web)
    )

    img_efecto_render = cv2.resize(
        img_cv,
        (ancho_web, alto_web)
    )

    _, buffer_original = cv2.imencode(
        '.png',
        img_original_render
    )

    _, buffer_efecto = cv2.imencode(
        '.png',
        img_efecto_render
    )

    img_original_str = base64.b64encode(
        buffer_original
    ).decode()

    img_efecto_str = base64.b64encode(
        buffer_efecto
    ).decode()

    factor_zoom_movil = st.slider(
        "🔬 AJUSTE DE DISTANCIA DE ENFOQUE (ZOOM LUPA):",
        1.5, 8.0, 4.0, 0.5
    )

    st.markdown("### 🖥️ MINI MONITOR FLOTANTE")
    activar_mini_monitor = st.checkbox(
        "👁️ Activar mini monitor que sigue el puntero",
        value=True
    )

    # Cuando esta opción está activa, el monitor principal muestra
    # la fotografía ORIGINAL y los efectos solo aparecen en el mini monitor.
    efectos_solo_mini_monitor = st.checkbox(
        "🧪 Mostrar efectos únicamente en el mini monitor",
        value=False,
        help=(
            "Activado: imagen principal sin filtros y mini monitor con "
            "los efectos forenses seleccionados. "
            "Desactivado: ambos muestran la imagen procesada."
        )
    )

    factor_zoom_mini = st.slider(
        "🔍 ZOOM DEL MINI MONITOR (0 = SOLO EFECTO / + = MÁS ZOOM):",
        0.0, 12.0, 4.0, 0.5,
        help=(
            "0 = sin ampliación: el mini monitor funciona como una ventana "
            "que revela el efecto exactamente sobre la zona donde pasa el puntero. "
            "Valores mayores a 0 = amplían la zona analizada."
        )
    )

    html_layout = f"""
    <div style="display: flex; flex-direction: column; align-items: center; gap: 20px; width: 100%;">
        <div class="panel-forense" style="width: 100%; max-width: 900px; background-color: #0f1115; border: 1px solid #1f242e; border-left: 4px solid #ff2222; padding: 15px; border-radius: 4px;">
            <p style="color: #ff2222; font-family: monospace; font-size: 13px; font-weight: bold; margin: 0 0 5px 0; text-transform: uppercase;">[MONITOR_ALPHA // VISOR DE CAMPO]</p>
            <p id="instrucciones" style="color: #00ff66; font-family: monospace; font-size: 11px; margin: 0 0 10px 0;">🟢 ESCANEO ACTIVO // Haz un clic en la foto para FIJAR las coordenadas de la lupa.</p>
            <div id="monitorContainer" style="position: relative; width: 100%; overflow: hidden;">
                <canvas id="evilCanvas" style="border: 1px solid #ff2222; background-color: #050505; width: 100%; display: block;"></canvas>

                <!-- MINI MONITOR FLOTANTE: sigue el puntero -->
                <canvas
                    id="miniMonitor"
                    width="220"
                    height="150"
                    style="
                        display: {'block' if activar_mini_monitor else 'none'};
                        position: absolute;
                        width: 220px;
                        height: 150px;
                        pointer-events: none;
                        border: 2px solid #00ff66;
                        background: #000;
                        box-shadow: 0 0 18px rgba(0, 255, 102, 0.75);
                        border-radius: 3px;
                        z-index: 20;
                        transform: translate(-50%, -115%);
                    ">
                </canvas>
            </div>
        </div>
        <div class="panel-forense" style="width: 100%; max-width: 330px; border-left: 4px solid #00ff66; padding: 15px; text-align: center; margin-bottom: 5px;">
            <p style="color: #00ff66; font-family: monospace; font-size: 13px; font-weight: bold; margin: 0 0 10px 0; text-transform: uppercase;">[SPECTRAL_ZOOM // LUPA DE OBJETIVO]</p>
            <canvas id="lupaCanvas" width="300" height="300" style="border: 1px solid #00ff66; background-color: #000; margin: 0 auto; display: block;"></canvas>
            <button onclick="descargarLupaLocal()" style="background: linear-gradient(135deg, #4a0000 0%, #1a0000 100%); color: #ff3333; width: 100%; border: 1px solid #ff2222; font-weight: bold; padding: 14px; margin-top: 15px; letter-spacing: 1px; text-transform: uppercase; font-family: 'Courier New', monospace; cursor: pointer; border-radius: 4px; box-shadow: 0 0 8px rgba(255, 34, 34, 0.2);">☣️ CONGELAR EVIDENCIA DE LUPA</button>
        </div>
    </div>
    <script>
        const canvas = document.getElementById('evilCanvas');
        const ctx = canvas.getContext('2d');

        const monitorContainer = document.getElementById('monitorContainer');
        const miniMonitor = document.getElementById('miniMonitor');
        const miniCtx = miniMonitor.getContext('2d', {{ willReadFrequently: true }});

        const lupaCanvas = document.getElementById('lupaCanvas');
        const lupaCtx = lupaCanvas.getContext('2d', {{ willReadFrequently: true }});

        const txtInstrucciones = document.getElementById('instrucciones');

        let mouseX = parseFloat(localStorage.getItem('evil_x')) || 450;
        let mouseY = parseFloat(localStorage.getItem('evil_y')) || 253;

        let zoomFactor = {factor_zoom_movil};
        let miniZoomFactor = {factor_zoom_mini};

        const miniMonitorActivo = {'true' if activar_mini_monitor else 'false'};
        let miraBloqueada = localStorage.getItem('evil_lock') === 'true';
        // ---------------------------------------------------------
        // MONITOR_ALPHA CON TAMAÑO PREDETERMINADO
        // ---------------------------------------------------------
        const MONITOR_WIDTH = 900;
        const MONITOR_HEIGHT = 506;

        // true = monitor principal ORIGINAL + mini monitor PROCESADO
        // false = ambos muestran la imagen PROCESADA
        const efectosSoloMiniMonitor = {'true' if efectos_solo_mini_monitor else 'false'};

        // Imagen original, sin ningún efecto aplicado.
        const imgOriginal = new Image();

        // Imagen con todos los efectos/filtros seleccionados.
        const imgEfecto = new Image();

        // Canvas invisible que contiene la versión procesada exactamente
        // con el mismo tamaño y posición que el monitor principal.
        const effectCanvas = document.createElement('canvas');
        effectCanvas.width = MONITOR_WIDTH;
        effectCanvas.height = MONITOR_HEIGHT;
        const effectCtx = effectCanvas.getContext('2d', {{
            willReadFrequently: true
        }});

        let imagenesListas = 0;

        function cuandoImagenLista() {{
            imagenesListas++;

            if (imagenesListas < 2) return;

            canvas.width = MONITOR_WIDTH;
            canvas.height = MONITOR_HEIGHT;

            if (miraBloqueada) {{
                txtInstrucciones.innerHTML =
                    "🔒 COORDENADAS FIJADAS // Objetivo inmóvil. Presiona el botón rojo de captura abajo.";
                txtInstrucciones.style.color = "#ff2222";
            }}

            draw();
        }}

        imgOriginal.onload = cuandoImagenLista;
        imgEfecto.onload = cuandoImagenLista;

        imgOriginal.src = "data:image/png;base64,{img_original_str}";
        imgEfecto.src = "data:image/png;base64,{img_efecto_str}";


        // Dibuja cualquier imagen dentro del monitor fijo sin deformarla.
        function dibujarImagenEnMonitor(
            contexto,
            imagen,
            anchoDestino,
            altoDestino
        ) {{
            contexto.clearRect(
                0,
                0,
                anchoDestino,
                altoDestino
            );

            contexto.fillStyle = "#000000";
            contexto.fillRect(
                0,
                0,
                anchoDestino,
                altoDestino
            );

            const escala = Math.min(
                anchoDestino / imagen.width,
                altoDestino / imagen.height
            );

            const anchoDibujo = imagen.width * escala;
            const altoDibujo = imagen.height * escala;

            const offsetX =
                (anchoDestino - anchoDibujo) / 2;

            const offsetY =
                (altoDestino - altoDibujo) / 2;

            contexto.drawImage(
                imagen,
                offsetX,
                offsetY,
                anchoDibujo,
                altoDibujo
            );
        }}


        function draw() {{
            // Siempre preparar la versión con EFECTOS en el canvas oculto.
            dibujarImagenEnMonitor(
                effectCtx,
                imgEfecto,
                MONITOR_WIDTH,
                MONITOR_HEIGHT
            );

            // Elegir qué se muestra en el monitor principal.
            const imagenPrincipal =
                efectosSoloMiniMonitor
                    ? imgOriginal
                    : imgEfecto;

            dibujarImagenEnMonitor(
                ctx,
                imagenPrincipal,
                canvas.width,
                canvas.height
            );

            actualizarLupa();
        }}
        function actualizarLupa() {{
            lupaCtx.clearRect(0, 0, lupaCanvas.width, lupaCanvas.height);
            lupaCtx.imageSmoothingEnabled = false;

            let size = 300 / zoomFactor;

            lupaCtx.drawImage(
                canvas,
                mouseX - size / 2,
                mouseY - size / 2,
                size,
                size,
                0,
                0,
                300,
                300
            );
        }}

        function actualizarMiniMonitor(clientX, clientY) {{
            if (!miniMonitorActivo) return;

            const rect = canvas.getBoundingClientRect();

            // Coordenadas del puntero dentro del monitor
            const localX = clientX - rect.left;
            const localY = clientY - rect.top;

            // El mini monitor sigue el puntero visualmente
            miniMonitor.style.left = `${{localX}}px`;
            miniMonitor.style.top = `${{localY}}px`;

            // Convertir coordenadas CSS a coordenadas reales del canvas
            const canvasX = localX * (canvas.width / rect.width);
            const canvasY = localY * (canvas.height / rect.height);

            // -------------------------------------------------
            // MODOS DEL MINI MONITOR
            // -------------------------------------------------
            // miniZoomFactor == 0:
            //   Sin zoom. El mini monitor revela el EFECTO a escala real
            //   justo debajo del puntero, como una ventana de inspección.
            //
            // miniZoomFactor > 0:
            //   Zoom progresivo. Cuanto mayor sea el valor, más cerca
            //   se verá la zona analizada.
            const size =
                miniZoomFactor === 0
                    ? 220
                    : 220 / miniZoomFactor;

            miniCtx.clearRect(0, 0, miniMonitor.width, miniMonitor.height);
            miniCtx.fillStyle = "#000";
            miniCtx.fillRect(0, 0, miniMonitor.width, miniMonitor.height);

            miniCtx.imageSmoothingEnabled = false;

            // Fuente del mini monitor:
            //
            // ZOOM = 0:
            //   siempre revela el efecto a escala real al pasar sobre la foto.
            //
            // "Solo efectos en mini" activado:
            //   monitor principal ORIGINAL + mini monitor PROCESADO.
            //
            // Modo normal:
            //   mini monitor muestra lo mismo que el monitor principal.
            const fuenteMiniMonitor =
                (miniZoomFactor === 0 || efectosSoloMiniMonitor)
                    ? effectCanvas
                    : canvas;

            miniCtx.drawImage(
                fuenteMiniMonitor,
                canvasX - size / 2,
                canvasY - size / 2,
                size,
                size,
                0,
                0,
                miniMonitor.width,
                miniMonitor.height
            );

            // Retícula central
            const cx = miniMonitor.width / 2;
            const cy = miniMonitor.height / 2;

            miniCtx.strokeStyle = "#ff2222";
            miniCtx.lineWidth = 1;

            miniCtx.beginPath();
            miniCtx.moveTo(cx - 14, cy);
            miniCtx.lineTo(cx + 14, cy);
            miniCtx.moveTo(cx, cy - 14);
            miniCtx.lineTo(cx, cy + 14);
            miniCtx.stroke();

            // Indicador del modo especial "0 = SOLO EFECTO"
            if (miniZoomFactor === 0) {{
                miniCtx.fillStyle = "rgba(0, 0, 0, 0.72)";
                miniCtx.fillRect(0, 0, miniMonitor.width, 22);

                miniCtx.fillStyle = "#00ff66";
                miniCtx.font = "bold 10px monospace";
                miniCtx.fillText(
                    "EFECTO // ESCALA REAL",
                    10,
                    15
                );
            }}
        }}

        function actualizarPosicion(clientX, clientY) {{
            if (miraBloqueada) return;

            const rect = canvas.getBoundingClientRect();

            mouseX = (clientX - rect.left) * (canvas.width / rect.width);
            mouseY = (clientY - rect.top) * (canvas.height / rect.height);

            localStorage.setItem('evil_x', mouseX);
            localStorage.setItem('evil_y', mouseY);

            actualizarLupa();
            actualizarMiniMonitor(clientX, clientY);
        }}
        canvas.addEventListener('mousemove', function(e) {{
            // El mini monitor sigue el puntero incluso cuando la lupa grande
            // tiene sus coordenadas fijadas.
            actualizarMiniMonitor(e.clientX, e.clientY);

            if (!miraBloqueada) {{
                actualizarPosicion(e.clientX, e.clientY);
            }}
        }});
        canvas.addEventListener('click', function(e) {{ miraBloqueada = !miraBloqueada; localStorage.setItem('evil_lock', miraBloqueada); if (miraBloqueada) {{ txtInstrucciones.innerHTML = "🔒 COORDENADAS FIJADAS // Objetivo inmóvil. Presiona el botón rojo de captura abajo."; txtInstrucciones.style.color = "#ff2222"; }} else {{ txtInstrucciones.innerHTML = "🟢 ESCANEO ACTIVO // Haz un clic en la foto para FIJAR las coordenadas de la lupa."; txtInstrucciones.style.color = "#00ff66"; const rect = canvas.getBoundingClientRect(); mouseX = (e.clientX - rect.left) * (canvas.width / rect.width); mouseY = (e.clientY - rect.top) * (canvas.height / rect.height); localStorage.setItem('evil_x', mouseX); localStorage.setItem('evil_y', mouseY); actualizarLupa(); }} }});
        canvas.addEventListener('wheel', function(e) {{ e.preventDefault(); if (e.deltaY < 0) zoomFactor += 0.5; else zoomFactor -= 0.5; zoomFactor = Math.max(1.5, Math.min(10.0, zoomFactor)); actualizarLupa(); }});
        canvas.addEventListener('touchmove', function(e) {{
            if (e.touches.length == 1) {{
                e.preventDefault();

                actualizarMiniMonitor(
                    e.touches[0].clientX,
                    e.touches[0].clientY
                );

                if (!miraBloqueada) {{
                    actualizarPosicion(
                        e.touches[0].clientX,
                        e.touches[0].clientY
                    );
                }}
            }}
        }}, {{ passive: false }});
        canvas.addEventListener('touchstart', function(e) {{
            if (e.touches.length == 1) {{
                actualizarMiniMonitor(
                    e.touches[0].clientX,
                    e.touches[0].clientY
                );

                if (!miraBloqueada) {{
                    actualizarPosicion(
                        e.touches[0].clientX,
                        e.touches[0].clientY
                    );
                }}
            }}
        }});
        function descargarLupaLocal() {{ const link = document.createElement('a'); link.download = 'evil_evidence_lupa.png'; link.href = lupaCanvas.toDataURL("image/png"); link.click(); }}
    </script>
    """
    # --- ALTURA FIJA DEL VISOR ---
    # El monitor ya tiene un tamaño predeterminado, por lo que todo el
    # componente mantiene una altura constante para cualquier fotografía.
    altura_total_html = 1200

    st.components.v1.html(
        html_layout,
        height=altura_total_html,
        scrolling=False
    )
    # --- RENDERIZADO DEL PANEL DE ANÁLISIS FORENSE PERICIAL CRÍTICO ---
    if activar_lga or activar_prnu or activar_retinex:
        st.markdown('<div class="panel-forense" style="border-left: 4px solid #00ffff;">', unsafe_allow_html=True)
        st.markdown("<p style='color:#00ffff; font-size:12px; font-weight:bold; margin-top:0; font-family:monospace;'>🔬 REPORTE DE ANÁLISIS PERICIAL DE IMAGEN</p>", unsafe_allow_html=True)
        if activar_lga: st.info("📉 MAPEO LGA ACTIVO: Inspeccionando la continuidad de los gradientes lumínicos. Busque rupturas para detectar fotomontajes.")
        if activar_prnu: st.info("🎚️ DIAGNÓSTICO PRNU: Extrayendo la estática del ruido sensor. Las áreas editadas perderán la homogeneidad.")
        if activar_retinex: st.success("👁 CALIBRACIÓN CLAHE COMPLETADA: Sombras subexpuestas abiertas quirúrgicamente. Inspeccione con la lupa.")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- TELEMETRÍA PARANORMAL DE CONTROL ---
    if activar_orbes or activar_emf:
        st.markdown('<div class="panel-forense" style="border-left: 4px solid #ff2222;">', unsafe_allow_html=True)
        st.markdown("<p style='color:#ff2222; font-size:12px; font-weight:bold; margin-top:0; font-family:monospace;'>☣️ REGISTRO DE SEÑALES ESPECTRALES ACTIVAS</p>", unsafe_allow_html=True)
        if activar_orbes:
            if orbes_detectados > 0: st.success(f"🌌 ALERTA AL DETECTOR: Se aislaron {orbes_detectados} anomalía(s) de orbes flotantes de alta energía en la imagen.")
            else: st.info("🌌 Buscando partículas... No se registraron firmas esféricas lumínicas.")
        if activar_emf:
            nivel_emf = min(100.0, max(5.0, frecuencia_ruido_base * 2.2))
            st.markdown(f"<p style='color:#ccc; font-size:12px; font-family:monospace; margin:0 0 5px 0;'>📻 CANAL ELECTROMAGNÉTICO (EMF): <b>{round(nivel_emf, 2)} mG (milliGauss)</b></p>", unsafe_allow_html=True)
            st.progress(min(1.0, nivel_emf / 100.0), text="Campos de Frecuencia Fantasma Detectados")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- RECONOCIMIENTO BIOMÉTRICO ---
    if activar_biometria:
        st.markdown('<div class="panel-forense" style="border-left: 4px solid #00ff66;">', unsafe_allow_html=True)
        st.markdown("<p style='color:#00ff66; font-size:12px; font-weight:bold; margin-top:0; font-family:monospace;'>🧬 RECONOCIMIENTO BIOMÉTRICO QUANTUM (DNN NETWORK)</p>", unsafe_allow_html=True)
        if biometria_fallida: st.warning("⚠️ MODO ESPECTRAL ACTIVADO: Señal de red neuronal interceptada por ruido térmico...")
        elif len(rostros_detectados) > 0:
            st.success(f"🎯 Red neuronal SSD ResNet activa: Se identificaron {len(rostros_detectados)} rostro(s) en la matriz.")
            for r in rostros_detectados:
                st.markdown(f"""<p style="color:#ccc; font-size:12px; font-family:monospace; margin: 5px 0;"><b>• SUJETO #{r['id']}:</b> GÉNERO: <span style="color:#00ff66;">{r['genero']}</span> // EDAD REAL ESTIMADA: <span style="color:#00ff66;">{r['edad']} AÑOS</span> // ESTADO ANÍMICO: <span style="color:#ff3333;">{r['animo']}</span> // PRECISIÓN RADAR: <span style="color:#ffaa00;">{r['confianza']}%</span></p>""", unsafe_allow_html=True)
        else: st.warning("⚠️ ALERTA FORENSE: No se mapearon firmas faciales biológicas.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel-forense" style="border-left: 4px solid #fff; background-color: #0f1115; border: 1px solid #1f242e; padding: 15px; border-radius: 4px;">', unsafe_allow_html=True)
    st.markdown("<p style='color:#fff; font-size:12px; font-weight:bold; margin-top:0; font-family:monospace;'>📊 TELEMETRÍA DE COMPOSICIÓN FOTOGRÁFICA</p>", unsafe_allow_html=True)
    st.progress(min(1.0, (brillo + 100) / 200), text=f"Alteración Térmica Lumínica: {brillo}%")
    st.progress(min(1.0, (contraste - 1.0) / 2.0), text=f"Densidad de Pixeles Espectrales: {round(contraste,1)}x")
    st.progress(0.98, text="Probabilidad de Entidad / Anomalía Espectral Fotográfica")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown("""<div class="panel-forense" style="border-left: 4px solid #ffaa00; background-color: #0f1115; text-align: center;"><p style="color: #ffaa00; font-size: 13px; font-weight: bold; margin: 0; font-family: monospace;">🔮 SISTEMA EN ESPERA // Por favor, introduce una fotografía en el cargador superior para iniciar el escaneo espectral.</p></div>""", unsafe_allow_html=True)
# --- SISTEMA DE FORO Y CAJA DE COMENTARIOS PERSISTENTE ---
st.markdown("---")
st.markdown('<div class="panel-forense" style="border-left: 4px solid #ffaa00;">', unsafe_allow_html=True)
st.markdown("<p style='color:#ffaa00; font-size:13px; font-weight:bold; margin-top:0; font-family:monospace;'>💬 BITÁCORA DE INVESTIGADORES FORENSES (FORO EN VIVO)</p>", unsafe_allow_html=True)

archivo_comentarios = "comentarios_forenses.txt"

# Asegurar la creación e inicialización del canal físico de la base de datos
if not os.path.exists(archivo_comentarios):
    with open(archivo_comentarios, "w", encoding="utf-8") as f:
        f.write("👤 AGENTE CORE // Consola iniciada correctamente. Sistema listo para recibir reportes periciales.\\n")

# Interfaz táctica de captura de datos
with st.form("formulario_comentarios", clear_on_submit=True):
    col_nombre, col_vacio = st.columns([1, 1])
    with col_nombre:
        nombre_usuario = st.text_input("👤 INDICATIVO / NOMBRE DE AGENTE:", max_chars=30, placeholder="Ej: Agente_07")
    texto_comentario = st.text_area("📝 REPORTE FORENSE / COMENTARIO ESPECTRAL:", max_chars=300, placeholder="Escribe aquí tus hallazgos sobre la imagen...")
    boton_enviar = st.form_submit_button("☣️ REGISTRAR REPORTE EN BITÁCORA")

# Ejecución mecánica de guardado persistente en el disco duro (No desaparecen jamás)
if boton_enviar and nombre_usuario.strip() and texto_comentario.strip():
    nombre_limpio = nombre_usuario.replace("\n", " ").strip()
    texto_limpio = texto_comentario.replace("\n", " ").strip()
    with open(archivo_comentarios, "a", encoding="utf-8") as f:
        f.write(f"👤 {nombre_limpio} // {texto_limpio}\n")
    st.toast("☣️ Reporte encriptado e incrustado en la base de datos con éxito.")
    st.rerun()

# Lectura y renderizado holográfico de los mensajes históricos guardados en la base de datos
st.markdown("<p style='color:#888; font-size:11px; font-family:monospace; margin-bottom:10px;'>📜 ARCHIVOS HISTÓRICOS ALMACENADOS EN EL DISCO SERVIDOR:</p>", unsafe_allow_html=True)
if os.path.exists(archivo_comentarios):
    with open(archivo_comentarios, "r", encoding="utf-8") as f:
        lineas_comentarios = f.readlines()
    
    # Desplegar los mensajes en orden cronológico inverso (el más nuevo arriba)
    for c in reversed(lineas_comentarios):
        if "//" in c:
            partes = c.split("//", 1)
            st.markdown(f"""
                <div style="background-color: #06070a; border: 1px solid #131722; padding: 8px; border-radius: 3px; margin-bottom: 8px; font-family: monospace; font-size: 11px;">
                    <span style="color: #ffaa00; font-weight: bold;">{partes[0].strip()}</span><br>
                    <span style="color: #ccc; line-height: 1.4;">{partes[1].strip()}</span>
                </div>
            """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
