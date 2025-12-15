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
    .main-header {font-size: 2.5rem; color: #FF4B4B; font-weight: bold;}
    .sub-header {font-size: 1.5rem; color: #333;}
    .report-box {padding: 20px; border-radius: 10px; background-color: #f0f2f6; margin-bottom: 20px; border-left: 5px solid #FF4B4B;}
    .success-box {padding: 20px; border-radius: 10px; background-color: #e8fdf5; margin-bottom: 20px; border-left: 5px solid #28a745;}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: PROFILO & METODOLOGIA ---
st.sidebar.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=70)
st.sidebar.title("🧬 VitalSense AI")
st.sidebar.caption("Master MADMA Project Work")
st.sidebar.markdown("**Materia:** Data Driven Organisation")

st.sidebar.write("---")

# Selezione Persona (Target: Early Adopters)
user_type = st.sidebar.selectbox(
    "Select Persona (Early Adopter)",
    ["Francesco (Sportivo Amatoriale)", "Aurora (Focus Benessere)", "Serena (Paziente A Rischio)"]
)

st.sidebar.write("---")

# SEZIONE METODOLOGICA (Per l'esame)
with st.sidebar.expander("📚 Note Metodologiche (Esame)", expanded=True):
    st.markdown("""
    **Strategy:** Lean Startup
    **MVP Type:** Wizard of Oz (Simulazione)
    **Target:** Early Adopters (Curve di Rogers)
    **Goal:** Estrarre Valore da Dati Grezzi
    """)

st.sidebar.subheader("📂 Data Ingestion")
uploaded_file = st.sidebar.file_uploader("Carica Storia Clinica (PDF/IMG)", type=['pdf', 'png', 'jpg'])

# --- FUNZIONI DI SUPPORTO ---

def generate_fake_history(user_name):
    """Genera dati storici per mostrare il trend (Data Driven Decision)"""
    dates = pd.date_range(start='2024-01-01', periods=12, freq='ME')
    
    if "Francesco" in user_name:
        scores = np.linspace(60, 95, 12) + np.random.normal(0, 2, 12)
        trend_label = "📈 Trend: Performance in crescita (Upgrade User)"
    elif "Serena" in user_name:
        scores = np.linspace(80, 85, 12) + np.random.normal(0, 5, 12)
        trend_label = "🛡️ Trend: Sicurezza Clinica Mantenuta"
    else:
        scores = np.random.randint(70, 90, 12)
        trend_label = "📊 Trend: Attività Variabile"
        
    df = pd.DataFrame({'Data': dates, 'Safety Score': scores})
    return df, trend_label

# --- LOGICA APPLICAZIONE ---

def main():
    st.markdown("<h1 class='main-header'>VitalSense AI Dashboard</h1>", unsafe_allow_html=True)
    
    # Header Dinamico basato sul JTBD
    st.markdown(f"""
    <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 25px;'>
        <h3 style='margin:0; color: #444;'>Job To Be Done:</h3>
        <p style='font-size: 18px; margin:0;'>
        <i>"Non voglio solo tracciare i miei passi. Voglio la certezza matematica di allenarmi nella mia <b>Safe Zone</b> clinica."</i>
        </p>
    </div>
    """, unsafe_allow_html=True)

    if uploaded_file is None:
        show_empty_state()
    else:
        process_data(uploaded_file, user_type)

def show_empty_state():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.info("👋 **In attesa di Data Ingestion.** Carica un referto nella sidebar.")
        st.markdown("### Il Problema (The Pain)")
        st.write("I dati sanitari grezzi (PDF, Carta) non creano valore perché sono disconnessi dall'attività quotidiana.")
        
        st.markdown("### La Soluzione (The Gain)")
        st.write("VitalSense trasforma il dato grezzo in **Azione Sicura**.")
        
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3004/3004458.png", width=150, caption="Waiting for Input...")

def process_data(file, user):
    # Simulazione Processo ETL (Extract, Transform, Load)
    with st.spinner('🔄 Reading Raw Data (OCR)... Extracting Value...'):
        time.sleep(2) 
    
    # Logica differenziata (Data Driven)
    if "Serena" in user:
        risk_score = 85
        status = "⚠️ ATTENZIONE CLINICA"
        box_class = "report-box" # Rosso
        advice = "Rilevata ipertensione nel referto grezzo. L'AI ha ricalcolato i tuoi limiti."
        action = "⛔ STOP Corsa. ✅ SÌ Camminata veloce (Max 120 bpm)."
        max_bpm = 125
        data_value = "HIGH RISK DETECTED"
    elif "Francesco" in user:
        risk_score = 98
        status = "✅ PERFORMANCE MODE"
        box_class = "success-box" # Verde
        advice = "Analisi eccellenti. Upgrade dei parametri di allenamento."
        action = "🚀 Via libera per HIIT e Corsa di Resistenza."
        max_bpm = 180
        data_value = "OPTIMAL CONDITION"
    else:
        risk_score = 90
        status = "✅ STANDARD"
        box_class = "success-box"
        advice = "Parametri nella norma."
        action = "Mantenere attività aerobica standard."
        max_bpm = 160
        data_value = "NORMAL"

    # --- DASHBOARD DI VALORE ---
    st.markdown("---")
    st.subheader(f"Analisi per: {user}")
    
    # KPI Row
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Raw Data Processed", "1 Document", "PDF/IMG")
    kpi2.metric("Safety Score (AI)", f"{risk_score}/100", delta="Value Extracted")
    kpi3.metric("Training Status", data_value, delta_color="off")

    # Insight Box (Value Proposition)
    st.markdown(f"""
    <div class='{box_class}'>
        <h3>🤖 AI Actionable Insight</h3>
        <p><b>Dato Grezzo:</b> {advice}</p>
        <p style='font-size: 20px; font-weight: bold;'>👉 Azione Suggerita: {action}</p>
    </div>
    """, unsafe_allow_html=True)

    # Grafici
    c1, c2 = st.columns([1, 1])

    with c1:
        st.subheader("Real-Time Constraint (Safe Zone)")
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = max_bpm - 15, 
            title = {'text': "Battito Cardiaco Attuale"},
            gauge = {
                'axis': {'range': [None, 200]},
                'bar': {'color': "darkgray"},
                'steps': [
                    {'range': [0, max_bpm], 'color': "#28a745"}, # Verde
                    {'range': [max_bpm, 200], 'color': "#FF4B4B"}], # Rosso
                'threshold': {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': max_bpm}}))
        st.plotly_chart(fig_gauge, use_container_width=True)

    with c2:
        st.subheader("Evolution Over Time (Upgrade User)")
        df_hist, trend_text = generate_fake_history(user)
        fig_line = px.line(df_hist, x='Data', y='Safety Score', markers=True, title=trend_text)
        fig_line.update_traces(line_color='#FF4B4B' if "Serena" in user else '#28a745')
        st.plotly_chart(fig_line, use_container_width=True)

if __name__ == "__main__":
    main()
