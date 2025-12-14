import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.graph_objects as go
import plotly.express as px

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="VitalSense AI - MVP", layout="wide", page_icon="🧬")

# --- CSS CUSTOM ---
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #FF4B4B;}
    .report-box {padding: 20px; border-radius: 10px; background-color: #f0f2f6; margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("🧬 VitalSense AI")
st.sidebar.caption("Master MADMA Project Work")
st.sidebar.markdown("**Materia:** Data Driven Organisation")
st.sidebar.write("---")

user_type = st.sidebar.selectbox(
    "Seleziona Persona (Target)",
    ["Francesco (Sportivo Amatoriale)", "Aurora (Focus Benessere)", "Serena (Paziente A Rischio)"]
)

st.sidebar.subheader("📂 Data Ingestion")
uploaded_file = st.sidebar.file_uploader("Carica Storia Clinica (PDF/IMG)", type=['pdf', 'png', 'jpg'])

# --- FUNZIONI DI SUPPORTO ---

def generate_fake_history(user_name):
    """Genera dati storici falsi per mostrare il trend nel tempo"""
    dates = pd.date_range(start='2024-01-01', periods=12, freq='ME') # Ultimi 12 mesi
    
    if "Francesco" in user_name:
        # Trend in miglioramento (Performance sale)
        scores = np.linspace(60, 95, 12) + np.random.normal(0, 2, 12)
        trend_label = "📈 Trend: Miglioramento Costante (+35%)"
    elif "Serena" in user_name:
        # Trend stabile/sicuro (Controllo rischi)
        scores = np.linspace(80, 85, 12) + np.random.normal(0, 5, 12) # Più oscillazione
        trend_label = "🛡️ Trend: Stabilità Clinica Mantenuta"
    else:
        # Random per Aurora
        scores = np.random.randint(70, 90, 12)
        trend_label = "📊 Trend: Attività Variabile"
        
    df = pd.DataFrame({'Data': dates, 'Safety Score': scores})
    return df, trend_label

# --- LOGICA APPLICAZIONE ---

def main():
    st.markdown("<h1 class='main-header'>VitalSense AI Dashboard</h1>", unsafe_allow_html=True)
    st.markdown(f"**Benvenuto/a, {user_type.split()[0]}** | *Digital Twin Status: Active*")
    
    with st.expander("ℹ️ Project Framework (Per il Docente)"):
        st.write("""
        **Materia:** Data Driven Organisation
        **Jobs to be Done:** Trasformare dati clinici statici in sicurezza dinamica.
        **Target:** Sportivi, Pazienti cronici, Health-conscious.
        **Tecnologia:** OCR + NLP + Predictive Algorithms + Time Series Analysis.
        """)

    st.write("---")

    if uploaded_file is None:
        show_empty_state()
    else:
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
        st.image("https://cdn-icons-png.flaticon.com/512/3004/3004458.png", width=150)

def process_data(file, user):
    with st.spinner('🔄 Analisi OCR e NLP in corso... Estrazione parametri vitali...'):
        time.sleep(1.5)
    
    st.success("✅ Analisi Completata! Profilo di Sicurezza Aggiornato.")
    
    # DATI SIMULATI
    if "Serena" in user:
        risk_score = 85
        status = "⚠️ ATTENZIONE"
        color = "red"
        advice = "Rilevata ipertensione nel referto. Corsa vietata. Camminata max 5km/h."
        max_bpm = 125
    elif "Francesco" in user:
        risk_score = 98
        status = "⚡ PERFORMANCE MODE"
        color = "green"
        advice = "Analisi eccellenti. Abilitato programma HIIT ad alta intensità."
        max_bpm = 180
    else:
        risk_score = 90
        status = "✅ OTTIMALE"
        color = "blue"
        advice = "Parametri nella norma. Mantenere attività aerobica standard."
        max_bpm = 160

    # DASHBOARD KPI
    col1, col2, col3 = st.columns(3)
    col1.metric("Safety Score", f"{int(risk_score)}/100", delta_color="inverse")
    col2.metric("Battito Max", f"{max_bpm} bpm")
    col3.metric("Status", status)

    # BOX CONSIGLIO
    st.markdown(f"""
    <div class='report-box' style='border-left: 5px solid {color}'>
        <h3>🤖 AI Coach Suggestion</h3>
        <p style='font-size: 18px'>{advice}</p>
    </div>
    """, unsafe_allow_html=True)

    # DUE GRAFICI AFFIANCATI (TACHIMETRO + STORICO)
    c1, c2 = st.columns([1, 1])

    with c1:
        st.subheader("Real-Time Monitor")
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = max_bpm - 20, # Valore attuale simulato
            title = {'text': "Battito Attuale"},
            gauge = {
                'axis': {'range': [None, 200]},
                'bar': {'color': "darkgray"},
                'steps': [
                    {'range': [0, max_bpm], 'color': "lightgreen"},
                    {'range': [max_bpm, 200], 'color': "red"}],
                'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': max_bpm}}))
        st.plotly_chart(fig_gauge, use_container_width=True)

    with c2:
        st.subheader("Data Driven Trends")
        # Generiamo lo storico
        df_hist, trend_text = generate_fake_history(user)
        
        fig_line = px.line(df_hist, x='Data', y='Safety Score', markers=True)
        fig_line.update_layout(yaxis_range=[50, 100], title=trend_text)
        st.plotly_chart(fig_line, use_container_width=True)

if __name__ == "__main__":
    main()
