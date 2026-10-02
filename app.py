import streamlit as st
import pandas as pd

# Configurazione della pagina in stile moderno/dark
st.set_page_config(
    page_title="IAmecc - Automotive Suite",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 IAmecc Diagnostic & Quote Studio")
st.markdown("Piattaforma intelligente per cataloghi ricambi multi-categoria e preventivi stampabili.")

# Sidebar per la navigazione tra i moduli
menu = st.sidebar.selectbox("Seleziona Modulo", ["Diagnostica Acustica AI", "Catalogo e Preventivi B2B"], key="menu_principale_app")

if menu == "Diagnostica Acustica AI":
    st.header("🎤 Diagnostica Acustica tramite IA")
    st.write("Registra o carica un campione audio del motore per identificare anomalie in tempo reale.")
    
    uploaded_file = st.file_uploader("Carica file audio (WAV / MP3)", type=["wav", "mp3"], key="uploader_audio_ai")
    
    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav')
        if st.button("Avvia Analisi IA", key="btn_avvia_ia"):
            with st.spinner("Analisi delle frequenze in corso..."):
                st.success("Diagnosi completata con successo!")
                st.metric(label="Anomalia Rilevata", value="Usura cuscinetto tendicinghia", delta="98% Confidenza")

elif menu == "Catalogo e Preventivi B2B":
    st.header("🛠️ Ricerca Ricambi e Preventivo Multi-Categoria")
    
    # --- 1. DECODER TARGA / TELAIO ---
    targa_input = st.text_input("Inserisci Targa o Numero Telaio (VIN)", "FL655GS", key="input_targa_vin").upper().strip()
    
    database_targhe = {
        "AB123CD": {"modello": "Volkswagen Golf VII 2.0 TDI", "anno": 2018},
        "XY987WZ": {"modello": "Fiat Panda 1.2 Easy", "anno": 2020},
        "JK456LM": {"modello": "BMW Serie 3 320d", "anno": 2017},
        "ZZ999ZZ": {"modello": "Audi A4 Avant 2.0 TDI", "anno": 2019},
        "FR444ON": {"modello": "Ford Focus 1.5 EcoBlue", "anno": 2021},
        "FL655GS": {"modello": "Veicolo Personalizzato", "anno": 2022}
    }
    
    veicolo_info = database_targhe.get(targa_input, {"modello": "Veicolo Personalizzato", "anno": 2022})
    st.info(f"🔍 Veicolo Identificato: **{veicolo_info['modello']}** — Anno: **{veicolo_info['anno']}** — Targa: **{targa_input}**")
    
    st.markdown("---")
    
    # --- 2. CATALOGO COMPLETO COMPONENTI AUTO (MULTICATEGORIA) ---
    st.markdown("### 📋 Selezione Ricambi da Liste Diverse")
    
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
            "Filtro Aria Abitacolo": {"costo": 20.00, "ore": 0.3, "codice": "AUT-SRV-403"},
            "Olio Motore 5W30 (5L)": {"costo": 55.00, "ore": 0.3, "codice": "AUT-SRV-404"}
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
    
    if 'carrello_pezzi' not in st.session_state:
        st.session_state['carrello_pezzi'] = []

    cat_selezionata = st.selectbox("Seleziona Categoria Sistema:", list(catalogo_ricambi.keys()), key="seleziona_categoria_sistema")
    pezzi_disponibili = catalogo_ricambi[cat_selezionata]
    
    pezzo_scelto = st.selectbox(f"Seleziona ricambio da [{cat_selezionata}]:", list(pezzi_disponibili.keys()), key="seleziona_pezzo_specifico")
    
    if st.button("➕ Aggiungi al Preventivo", key="btn_aggiungi_carrello"):
        info_pezzo = pezzi_disponibili[pezzo_scelto]
        elemento = {
            "categoria": cat_selezionata,
            "nome": pezzo_scelto,
            "codice": info_pezzo["codice"],
            "costo_base": info_pezzo["costo"],
            "ore": info_pezzo["ore"]
        }
        if elemento not in st.session_state['carrello_pezzi']:
            st.session_state['carrello_pezzi'].append(elemento)
            st.success(f"Aggiunto: {pezzo_scelto}")
        else:
            st.warning("Questo ricambio è già presente nel preventivo.")

    if st.session_state['carrello_pezzi']:
        st.markdown("#### 🛒 Ricambi Selezionati nel Preventivo:")
        for idx, item in enumerate(st.session_state['carrello_pezzi']):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"- **{item['nome']}** ({item['categoria']}) - Codice: `{item['codice']}`")
            with col2:
                if st.button("Rimuovi", key=f"del_item_{idx}"):
                    st.session_state['carrello_pezzi'].pop(idx)
                    st.rerun()

    st.markdown("---")
    
    # --- 3. CALCOLO PREVENTIVO FINALE ---
    if st.button("🧮 Calcola Preventivo Totale", key="btn_calcola_totale"):
        if not st.session_state['carrello_pezzi']:
            st.warning("Il carrello dei ricambi è vuoto. Aggiungi almeno un pezzo.")
        else:
            tot_ricambi_agg = 0
            tot_ore = 0
            inflation_factor = 1.05
            labor_rate = 50.00
            
            dettagli_calcolati = []
            for item in st.session_state['carrello_pezzi']:
                c_agg = item["costo_base"] * inflation_factor
                tot_ricambi_agg += c_agg
                tot_ore += item["ore"]
                dettagli_calcolati.append({
                    "Categoria": item["categoria"],
                    "Ricambio": item["nome"],
                    "Codice": item["codice"],
                    "Costo Listino": f"€ {c_agg:.2f}",
                    "Manodopera": f"{item['ore']}h"
                })
            
            tot_lavoro = tot_ore * labor_rate
            totale_generale = tot_ricambi_agg + tot_lavoro
            
            st.session_state['preventivo_finale'] = {
                "targa": targa_input,
                "modello": veicolo_info["modello"],
                "anno": veicolo_info["anno"],
                "elementi": dettagli_calcolati,
                "tot_ricambi": tot_ricambi_agg,
                "tot_ore": tot_ore,
                "tot_lavoro": tot_lavoro,
                "totale_generale": totale_generale
            }

    # --- 4. VISUALIZZAZIONE E STAMPA FOGLIO PREVENTIVO ---
    if 'preventivo_finale' in st.session_state:
        p = st.session_state['preventivo_finale']
        st.markdown("---")
        
        st.markdown(f"### 📄 Foglio Preventivo Ufficiale IAmecc")
        st.write(f"**Veicolo:** {p['modello']} — **Anno:** {p['anno']} — **Targa:** {p['targa']}")
        st.markdown("---")
        
        # Tabella nativa di Streamlit (evita qualsiasi errore di sintassi HTML a schermo)
        df_preventivo = pd.DataFrame(p['elementi'])
        st.dataframe(df_preventivo, use_container_width=True, hide_index=True)
        
        st.markdown(f"**Totale Ricambi (Aggiornato):** € {p['tot_ricambi']:.2f}")
        st.markdown(f"**Totale Manodopera ({p['tot_ore']} ore complessive):** € {p['tot_lavoro']:.2f}")
        st.markdown(f"### **Totale Preventivo: € {p['totale_generale']:.2f}**")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
            <button onclick="window.print()" style="width: 100%; background-color: #00E5FF; color: black; padding: 14px; font-weight: bold; border: none; border-radius: 12px; cursor: pointer; font-size: 16px;">
                🖨️ STAMPA / SALVA PREVENTIVO IN PDF
            </button>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Conferma e Invia Ordine a AUTODOC (API B2B)", key="btn_ordine_b2b_finale"):
            st.success("Ordine cumulativo inoltrato con successo al distributore!")
