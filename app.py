import streamlit as st
import pandas as pd

# Configurazione della pagina in stile moderno/dark
st.set_page_config(
    page_title="IAmecc - Automotive Suite",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 IAmecc Diagnostic & Quote Studio")
st.markdown("Piattaforma intelligente per diagnosi acustica, cataloghi ricambi e preventivi anti-rincari.")

# Sidebar per la navigazione tra i moduli
menu = st.sidebar.selectbox("Seleziona Modulo", ["Diagnostica Acustica AI", "Catalogo e Preventivi B2B"])

if menu == "Diagnostica Acustica AI":
    st.header("🎤 Diagnostica Acustica tramite IA")
    st.write("Registra o carica un campione audio del motore per identificare anomalie in tempo reale.")
    
    uploaded_file = st.file_uploader("Carica file audio (WAV / MP3)", type=["wav", "mp3"])
    
    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav')
        if st.button("Avvia Analisi IA"):
            with st.spinner("Analisi delle frequenze in corso..."):
                # Simulazione esito IA
                st.success("Diagnosi completata con successo!")
                st.metric(label="Anomalia Rilevata", value="Usura cuscinetto tendicinghia", delta="98% Confidenza")

elif menu == "Catalogo e Preventivi B2B":
    st.header("🛠️ Ricerca Ricambi e Preventivo Dinamico")
    
    vin_targa = st.text_input("Inserisci Targa o Numero Telaio (VIN)", "AB123CD")
    
    if st.button("Cerca Schemi e Listini"):
        st.info(f"Decodifica veicolo {vin_targa} tramite database TecDoc...")
        
        # Dati simulati del ricambio e preventivo
        part_cost = 135.50
        labor_hours = 2.5
        labor_rate = 50.00
        inflation_factor = 1.05 # Adeguamento anti-rincari
        
        adjusted_part = part_cost * inflation_factor
        total_labor = labor_hours * labor_rate
        final_total = adjusted_part + total_labor
        
        st.markdown("---")
        st.subheader("Foglio Preventivo Ufficiale")
        st.write(f"**Ricambio Selezionato:** Kit Cinghia Distribuzione (Codice: AUT-KT-98765)")
        st.write(f"**Costo Ricambio (Listino aggiornato):** € {adjusted_part:.2f}")
        st.write(f"**Costo Manodopera ({labor_hours}h):** € {total_labor:.2f}")
        st.markdown(f"### **Totale Preventivo: € {final_total:.2f}**")
        
        if st.button("Conferma e Invia Ordine a AUTODOC (API B2B)"):
            st.success("Ordine inoltrato con successo al distributore!")
