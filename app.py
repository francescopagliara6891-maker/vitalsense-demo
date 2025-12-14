import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.graph_objects as go

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="VitalSense AI - MVP", layout="wide", page_icon="🧬")

# --- CSS CUSTOM (Per renderla professionale) ---
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #FF4B4B;}
    .report-box {padding: 20px; border-radius: 10px; background-color: #f0f2f6; margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: PROFILO & UPLOAD ---
st.sidebar.title("🧬 VitalSense AI")
st.sidebar.caption("Master MADMA Project Work")
st.sidebar.write("---")

# Selezione Utente (Simulazione Persona)
user_type = st.sidebar.selectbox(
    "Seleziona Persona (Target)",
    ["Francesco (Sportivo Amatoriale)", "Aurora (Focus Benessere)", "Mario (Paziente Cronico)"]
)

st.sidebar.subheader("📂 Data Ingestion")
uploaded_file = st.sidebar.file_uploader("Carica Storia Clinica (PDF/IMG)", type=['pdf', 'png', 'jpg'])

# --- LOGICA APPLICAZIONE ---

def main():
    # Intestazione
    st.markdown("<h1 class='main-header'>VitalSense AI Dashboard</h1>", unsafe_allow_html=True)
    st.markdown(f"**Benvenuto, {user_type.split()[0]}** | *Digital Twin Status: Active*")
    
    # 1. SEZIONE TEORICA (Qui integreremo i tuoi appunti man mano!)
    with st.expander("ℹ️ Project Framework (Per il Docente)"):
        st.write("""
        **Jobs to be Done:** Trasformare dati clinici statici in sicurezza dinamica.
        **Target:** Sportivi, Pazienti cronici, Health-conscious.
        **Tecnologia:** OCR + NLP + Predictive Algorithms.
        """)

    st.write("---")

    # 2. SEZIONE OPERATIVA (DEMO)
    if uploaded_file is None:
        # STATO INIZIALE (Senza dati)
        show_empty_state()
    else:
        # STATO ATTIVO (Con dati simulati)
        process_data(uploaded_file, user_type)

def show_empty_state():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.info("👋 **In attesa di input.** Carica un referto medico nella barra laterale per attivare l'AI.")
        st.markdown("### Cosa fa VitalSense?")
        st.markdown("""
        1. **Analizza** documenti non strutturati (OCR).
        2. **Estrae** vincoli clinici (es. aritmie, carenze).
        3. **Calcola** la tua 'Safe Zone' per l'allenamento.
        """)
    with col2:
        # Un grafico vuoto o statico
        st.image("https://cdn-icons-png.flaticon.com/512/3004/3004458.png", width=150)

def process_data(file, user):
    # Simulazione caricamento
    with st.spinner('🔄 Analisi OCR e NLP in corso... Estrazione parametri vitali...'):
        time.sleep(2) # Effetto scenico
    
    st.success("✅ Analisi Completata! Profilo di Sicurezza Aggiornato.")
    
    # DATI SIMULATI IN BASE ALL'UTENTE
    if "Mario" in user:
        risk_score = 85
        status = "⚠️ ATTENZIONE"
        color = "red"
        advice = "Rilevata ipertensione nel referto. Corsa vietata. Camminata max 5km/h."
        max_bpm = 125
    else:
        risk_score = 10
        status = "✅ OTTIMALE"
        color = "green"
        advice = "Parametri ematici perfetti. Via libera per allenamento cardio intenso."
        max_bpm = 175

    # DASHBOARD RISULTATI
    col1, col2, col3 = st.columns(3)
    col1.metric("Livello di Rischio", f"{risk_score}/100", delta_color="inverse")
    col2.metric("Battito Max Sicuro", f"{max_bpm} bpm")
    col3.metric("Status Clinico", status)

    st.markdown(f"""
    <div class='report-box' style='border-left: 5px solid {color}'>
        <h3>🤖 AI Coach Suggestion</h3>
        <p style='font-size: 18px'>{advice}</p>
    </div>
    """, unsafe_allow_html=True)

    # GRAFICO TACHIMETRO
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 90, # Valore attuale finto
        title = {'text': "Monitoraggio Real-Time"},
        gauge = {
            'axis': {'range': [None, 200]},
            'bar': {'color': "lightgray"},
            'steps': [
                {'range': [0, max_bpm], 'color': "lightgreen"},
                {'range': [max_bpm, 200], 'color': "red"}],
            'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': max_bpm}}))
    
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()