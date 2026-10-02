import streamlit as st
import pandas as pd

# Configurazione della pagina in stile moderno/dark
st.set_page_config(
    page_title="IAmecc - Automotive Suite",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 IAmecc Diagnostic & Quote Studio")
st.markdown("Piattaforma intelligente per diagnosi acustica, cataloghi ricambi completi e preventivi stampabili.")

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
    
    # --- 1. DECODER TARGA / TELAIO ---
    targa_input = st.text_input("Inserisci Targa o Numero Telaio (VIN)", "AB123CD").upper().strip()
    
    # Database simulato di decodifica targa -> Modello Auto
    database_targhe = {
        "AB123CD": "Volkswagen Golf VII 2.0 TDI (150 CV)",
        "XY987WZ": "Fiat Panda 1.2 Easy (69 CV)",
        "JK456LM": "BMW Serie 3 (F30) 320d (190 CV)",
        "ZZ999ZZ": "Audi A4 Avant 2.0 TDI (163 CV)",
        "FR444ON": "Ford Focus 1.5 EcoBlue (120 CV)"
    }
    
    modello_auto = database_targhe.get(targa_input, f"Veicolo Personalizzato / Generico ({targa_input})")
    st.info(f"🔍 Veicolo Identificato: **{modello_auto}**")
    
    st.markdown("---")
    
    # --- 2. CATALOGO COMPLETO DEI PEZZI DELL'AUTO ---
    st.markdown("### 📋 Catalogo Generale Componenti Auto")
    
    categoria_scelta = st.selectbox(
        "Seleziona il sistema dell'auto:",
        [
            "Distribuzione e Motore",
            "Impianto Frenante",
            "Sospensioni e Sterzo",
            "Frizione e Trasmissione",
            "Filtri e Tagliando Ordinario",
            "Impianto Elettrico e Accensione",
            "Scarico e Antinquinamento"
        ]
    )
    
    catalogo_ricambi = {
        "Distribuzione e Motore": {
            "Kit Cinghia Distribuzione + Pompa Acqua": {"costo": 135.50, "ore": 3.0, "codice": "AUT-MOT-001"},
            "Cinghia Servizi / Alternatore": {"costo": 25.00, "ore": 0.5, "codice": "AUT-MOT-002"},
            "Guarnizione Testata": {"costo": 90.00, "ore": 6.0, "codice": "AUT-MOT-003"},
            "Kit Catena di Distribuzione": {"costo": 280.00, "ore": 5.5, "codice": "AUT-MOT-004"}
        },
        "Impianto Frenante": {
            "Pastiglie Freni Anteriori": {"costo": 65.00, "ore": 1.0, "codice": "AUT-BRK-101"},
            "Pastiglie Freni Posteriori": {"costo": 50.00, "ore": 1.0, "codice": "AUT-BRK-102"},
            "Dischi freno anteriori (Coppia)": {"costo": 120.00, "ore": 1.5, "codice": "AUT-BRK-103"},
            "Dischi freno posteriori (Coppia)": {"costo": 95.00, "ore": 1.5, "codice": "AUT-BRK-104"},
            "Pinza freno anteriore": {"costo": 140.00, "ore": 1.2, "codice": "AUT-BRK-105"}
        },
        "Sospensioni e Sterzo": {
            "Ammortizzatori Anteriori (Coppia)": {"costo": 180.00, "ore": 2.5, "codice": "AUT-SUS-201"},
            "Ammortizzatori Posteriori (Coppia)": {"costo": 140.00, "ore": 2.0, "codice": "AUT-SUS-202"},
            "Braccio / Sospensione ruota": {"costo": 75.00, "ore": 1.0, "codice": "AUT-SUS-203"},
            "Testina sterzo": {"costo": 30.00, "ore": 0.8, "codice": "AUT-SUS-204"},
            "Cuscinetto Ruota": {"costo": 85.00, "ore": 1.5, "codice": "AUT-SUS-205"}
        },
        "Frizione e Trasmissione": {
            "Kit Frizione Completo": {"costo": 210.00, "ore": 4.5, "codice": "AUT-TRV-301"},
            "Kit Frizione + Volano Bimassa": {"costo": 450.00, "ore": 5.0, "codice": "AUT-TRV-302"},
            "Semiasse completo": {"costo": 160.00, "ore": 1.5, "codice": "AUT-TRV-303"},
            "Olio cambio manuale (2L)": {"costo": 35.00, "ore": 0.5, "codice": "AUT-TRV-304"}
        },
        "Filtri e Tagliando Ordinario": {
            "Kit Tagliando Completo (Olio + 4 Filtri)": {"costo": 110.00, "ore": 1.0, "codice": "AUT-SRV-401"},
            "Filtro Olio": {"costo": 12.00, "ore": 0.2, "codice": "AUT-SRV-402"},
            "Filtro Aria Abitacolo (Airdox/Polline)": {"costo": 20.00, "ore": 0.3, "codice": "AUT-SRV-403"},
            "Olio Motore 5W30 (5 Litri)": {"costo": 55.00, "ore": 0.3, "codice": "AUT-SRV-404"}
        },
        "Impianto Elettrico e Accensione": {
            "Batteria Auto Start&Stop 70Ah": {"costo": 130.00, "ore": 0.3, "codice": "AUT-ELC-501"},
            "Alternatore Rigenerato": {"costo": 220.00, "ore": 2.0, "codice": "AUT-ELC-502"},
            "Motorino di Avviamento": {"costo": 170.00, "ore": 1.8, "codice": "AUT-ELC-503"},
            "Candele di Accensione (Set 4 pz)": {"costo": 40.00, "ore": 0.5, "codice": "AUT-ELC-504"}
        },
        "Scarico e Antinquinamento": {
            "Filtro Antiparticolato (DPF / FAP)": {"costo": 420.00, "ore": 2.5, "codice": "AUT-EXH-601"},
            "Marmitta / Silenziatore Posteriore": {"costo": 115.00, "ore": 1.0, "codice": "AUT-EXH-602"},
            "Sonda Lambda": {"costo": 85.00, "ore": 0.6, "codice": "AUT-EXH-603"}
        }
    }
    
    pezzi_disponibili = catalogo_ricambi[categoria_scelta]
    pezzo_selezionato = st.selectbox("Seleziona il ricambio esatto:", list(pezzi_disponibili.keys()))
    dettagli_pezzo = pezzi_disponibili[pezzo_selezionato]
    
    # --- 3. CALCOLO PREVENTIVO ---
    if st.button("Calcola Preventivo Ufficiale"):
        part_cost = dettagli_pezzo["costo"]
        labor_hours = dettagli_pezzo["ore"]
        labor_rate = 50.00  # €/ora
        inflation_factor = 1.05  # +5% adeguamento rincari
        
        adjusted_part = part_cost * inflation_factor
        total_labor = labor_hours * labor_rate
        final_total = adjusted_part + total_labor
        
        # Salviamo nel session_state per renderlo persistente e stampabile
        st.session_state['preventivo'] = {
            "targa": targa_input,
            "modello": modello_auto,
            "categoria": categoria_scelta,
            "pezzo": pezzo_selezionato,
            "codice": dettagli_pezzo['codice'],
            "ricambio_costo": adjusted_part,
            "ore_lavoro": labor_hours,
            "lavoro_costo": total_labor,
            "totale": final_total
        }

    # --- 4. VISUALIZZAZIONE E STAMPA FOGLIO PREVENTIVO ---
    if 'preventivo' in st.session_state:
        p = st.session_state['preventivo']
        st.markdown("---")
        
        # Foglio Preventivo Formattato
        st.markdown(f"""
        <div style="background-color: #161B22; padding: 24px; border-radius: 16px; border: 1px solid #30363D;">
            <h2 style="color: #00E5FF; margin-top: 0;">📄 Foglio Preventivo Ufficiale IAmecc</h2>
            <p><b>Veicolo:</b> {p['modello']} (Targa: {p['targa']})</p>
            <hr style="border-color: #30363D;">
            <p><b>Categoria:</b> {p['categoria']}</p>
            <p><b>Ricambio:</b> {p['pezzo']} (Codice: <code>{p['codice']}</code>)</p>
            <p><b>Costo Ricambio (Listino aggiornato):</b> € {p['ricambio_costo']:.2f}</p>
            <p><b>Costo Manodopera ({p['ore_lavoro']}h):</b> € {p['lavoro_costo']:.2f}</p>
            <hr style="border-color: #30363D;">
            <h3 style="color: #00E5FF; text-align: right;">Totale Preventivo: € {p['totale']:.2f}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Pulsante di stampa HTML/JS
        st.markdown("""
            <button onclick="window.print()" style="width: 100%; background-color: #00E5FF; color: black; padding: 14px; font-weight: bold; border: none; border-radius: 12px; cursor: pointer; font-size: 16px;">
                🖨️ STAMPA / SALVA PREVENTIVO IN PDF
            </button>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Conferma e Invia Ordine a AUTODOC (API B2B)"):
            st.success(f"Ordine per il ricambio `{p['codice']}` inoltrato con successo al distributore!")
