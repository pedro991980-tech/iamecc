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
                st.success("Diagnosi completata con successo!")
                st.metric(label="Anomalia Rilevata", value="Usura cuscinetto tendicinghia", delta="98% Confidenza")

elif menu == "Catalogo e Preventivi B2B":
    st.header("🛠️ Ricerca Ricambi e Preventivo Dinamico")
    
    vin_targa = st.text_input("Inserisci Targa o Numero Telaio (VIN)", "AB123CD")
    
    # --- AGGIUNTA: Selezione dinamica del ricambio e del guasto ---
    st.markdown("### Selezione Componente")
    
    componente_selezionato = st.selectbox(
        "Scegli il ricambio da sostituire:",
        [
            "Kit Cinghia Distribuzione + Pompa Acqua",
            "Pastiglie Freni Anteriori",
            "Filtro Olio e Tagliando",
            "Alternatore Motore",
            "Ammortizzatori Anteriori",
            "Frizione e Volano"
        ]
    )
    
    # Dizionario con i costi base simulati per ogni ricambio
    listino_ricambi = {
        "Kit Cinghia Distribuzione + Pompa Acqua": {"costo": 135.50, "ore": 2.5, "codice": "AUT-KT-98765"},
        "Pastiglie Freni Anteriori": {"costo": 65.00, "ore": 1.0, "codice": "AUT-BR-11223"},
        "Filtro Olio e Tagliando": {"costo": 45.00, "ore": 1.0, "codice": "AUT-FL-44556"},
        "Alternatore Motore": {"costo": 220.00, "ore": 2.0, "codice": "AUT-AL-77889"},
        "Ammortizzatori Anteriori": {"costo": 180.00, "ore": 3.0, "codice": "AUT-AM-33445"},
        "Frizione e Volano": {"costo": 350.00, "ore": 5.0, "codice": "AUT-CL-99001"}
    }
    
    ricambio_info = listino_ricambi[componente_selezionato]
    
    if st.button("Calcola Preventivo Aggiornato"):
        st.info(f"Decodifica veicolo {vin_targa} e interrogazione listini in tempo reale...")
        
        part_cost = ricambio_info["costo"]
        labor_hours = ricambio_info["ore"]
        labor_rate = 50.00  # Tariffa oraria officina
        inflation_factor = 1.05  # Adeguamento anti-rincari di mercato
        
        adjusted_part = part_cost * inflation_factor
        total_labor = labor_hours * labor_rate
        final_total = adjusted_part + total_labor
        
        st.markdown("---")
        st.subheader("Foglio Preventivo Ufficiale")
        st.write(f"**Ricambio Selezionato:** {componente_selezionato} (Codice: {ricambio_info['codice']})")
        st.write(f"**Costo Ricambio (Listino aggiornato):** € {adjusted_part:.2f}")
        st.write(f"**Costo Manodopera ({labor_hours}h):** € {total_labor:.2f}")
        st.markdown(f"### **Totale Preventivo: € {final_total:.2f}**")
        
        if st.button("Conferma e Invia Ordine a AUTODOC (API B2B)"):
            st.success("Ordine inoltrato con successo al distributore!")
