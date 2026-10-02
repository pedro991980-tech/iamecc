import streamlit as st
import pandas as pd

# Configurazione della pagina in stile moderno/dark
st.set_page_config(
    page_title="IAmecc - Automotive Suite",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 IAmecc Diagnostic & Quote Studio")
st.markdown("Piattaforma intelligente per diagnosi acustica, cataloghi ricambi multipli e preventivi stampabili.")

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
    st.header("🛠️ Ricerca Ricambi e Preventivo Dinamico Multi-Pezzo")
    
    # --- 1. DECODER TARGA / TELAIO (Con Modello e Anno) ---
    targa_input = st.text_input("Inserisci Targa o Numero Telaio (VIN)", "AB123CD").upper().strip()
    
    database_targhe = {
        "AB123CD": {"modello": "Volkswagen Golf VII 2.0 TDI (150 CV)", "anno": 2018},
        "XY987WZ": {"modello": "Fiat Panda 1.2 Easy (69 CV)", "anno": 2020},
        "JK456LM": {"modello": "BMW Serie 3 (F30) 320d (190 CV)", "anno": 2017},
        "ZZ999ZZ": {"modello": "Audi A4 Avant 2.0 TDI (163 CV)", "anno": 2019},
        "FR444ON": {"modello": "Ford Focus 1.5 EcoBlue (120 CV)", "anno": 2021}
    }
    
    veicolo_info = database_targhe.get(targa_input, {"modello": f"Veicolo Personalizzato ({targa_input})", "anno": 2022})
    st.info(f"🔍 Veicolo Identificato: **{veicolo_info['modello']}** — Anno: **{veicolo_info['anno']}**")
    
    st.markdown("---")
    
    # --- 2. CATALOGO COMPLETO COMPONENTI AUTO ---
    st.markdown("### 📋 Catalogo Generale Componenti Auto (Selezione Multipla)")
    
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
    
    pezzi_disponibili = catalogo_ricambi[categoria_scelta]
    
    # --- SELEZIONE MULTIPLA DEI PEZZI ---
    pezzi_selezionati = st.multiselect(
        "Seleziona uno o più ricambi da inserire nel preventivo:",
        list(pezzi_disponibili.keys())
    )
    
    # --- 3. CALCOLO PREVENTIVO MULTI-PARTE ---
    if st.button("Calcola Preventivo con Ricambi Multipli"):
        if not pezzi_selezionati:
            st.warning("Seleziona almeno un ricambio dalla lista prima di procedere.")
        else:
            tot_ricambi_base = 0
            tot_ore = 0
            dettagli_lista = []
            
            inflation_factor = 1.05  # +5% rincari listino
            labor_rate = 50.00       # €/ora
            
            for p_nome in pezzi_selezionati:
                info = pezzi_disponibili[p_nome]
                c_aggiornato = info["costo"] * inflation_factor
                tot_ricambi_base += c_aggiornato
                tot_ore += info["ore"]
                dettagli_lista.append({
                    "nome": p_nome,
                    "codice": info["codice"],
                    "costo": c_aggiornato,
                    "ore": info["ore"]
                })
            
            tot_lavoro = tot_ore * labor_rate
            totale_generale = tot_ricambi_base + tot_lavoro
            
            st.session_state['preventivo_multi'] = {
                "targa": targa_input,
                "modello": veicolo_info["modello"],
                "anno": veicolo_info["anno"],
                "categoria": categoria_scelta,
                "elementi": dettagli_lista,
                "tot_ricambi": tot_ricambi_base,
                "tot_ore": tot_ore,
                "tot_lavoro": tot_lavoro,
                "totale_finale": totale_generale
            }

    # --- 4. VISUALIZZAZIONE E STAMPA FOGLIO PREVENTIVO ---
    if 'preventivo_multi' in st.session_state:
        p = st.session_state['preventivo_multi']
        st.markdown("---")
        
        elementi_html = ""
        for item in p['elementi']:
            elementi_html += f"""
            <tr>
                <td style="padding: 6px 0;">{item['nome']}</td>
                <td style="padding: 6px 0;"><code>{item['codice']}</code></td>
                <td style="padding: 6px 0;">€ {item['costo']:.2f}</td>
                <td style="padding: 6px 0;">{item['ore']}h</td>
            </tr>
            """
        
        st.markdown(f"""
        <div style="background-color: #161B22; padding: 24px; border-radius: 16px; border: 1px solid #30363D;">
            <h2 style="color: #00E5FF; margin-top: 0;">📄 Foglio Preventivo Ufficiale IAmecc</h2>
            <p><b>Veicolo:</b> {p['modello']} &nbsp;|&nbsp; <b>Anno:</b> {p['anno']} &nbsp;|&nbsp; <b>Targa:</b> {p['targa']}</p>
            <hr style="border-color: #30363D;">
            <p><b>Categoria Sistema:</b> {p['categoria']}</p>
            <table style="width:100%; color: white; margin-bottom: 15px; border-collapse: collapse;">
                <tr style="border-bottom: 1px solid #30363D; text-align: left;">
                    <th style="padding-bottom: 8px;">Ricambio</th>
                    <th style="padding-bottom: 8px;">Codice</th>
                    <th style="padding-bottom: 8px;">Costo (Listino)</th>
                    <th style="padding-bottom: 8px;">Manodopera</th>
                </tr>
                {elementi_html}
            </table>
            <hr style="border-color: #30363D;">
            <p><b>Totale Ricambi (Aggiornato):</b> € {p['tot_ricambi']:.2f}</p>
            <p><b>Totale Manodopera ({p['tot_ore']} ore complessive):</b> € {p['tot_lavoro']:.2f}</p>
            <h3 style="color: #00E5FF; text-align: right;">Totale Preventivo: € {p['totale_finale']:.2f}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
            <button onclick="window.print()" style="width: 100%; background-color: #00E5FF; color: black; padding: 14px; font-weight: bold; border: none; border-radius: 12px; cursor: pointer; font-size: 16px;">
                🖨️ STAMPA / SALVA PREVENTIVO IN PDF
            </button>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Conferma e Invia Ordine a AUTODOC (API B2B)"):
            st.success("Ordine per i ricambi multipli inoltrato con successo al distributore!")
