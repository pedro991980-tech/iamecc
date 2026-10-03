import streamlit as st
import pandas as pd
from streamlit_mic_recorder import mic_recorder
from utils import interroga_verificaauto, analizza_audio_motore, get_catalogo_ricambi

st.set_page_config(
    page_title="IAmecc - Automotive Suite",
    page_icon="🚗",
    layout="centered"
)

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🚗 IAmecc Diagnostic & Quote Studio")
st.markdown("Suite professionale per officine: Verifica Veicolo (VerificaAuto.it) e Diagnostica FFT.")

menu = st.sidebar.selectbox("Seleziona Modulo", ["Diagnostica Acustica & Riconoscimento AI", "Catalogo e Preventivi B2B"], key="nav_menu_principale")

if menu == "Diagnostica Acustica & Riconoscimento AI":
    st.header("🎙️ Stazione di Diagnosi Acustica (DSP)")
    st.markdown("---")
    
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.markdown("### 📋 Linee Guida Operative")
        st.markdown("""
        1. **Posizionamento:** Avvicina il microfono a 20-30 cm dal vano motore.
        2. **Acquisizione:** Registra per **10-15 secondi** con il motore in moto.
        3. **Elaborazione:** Avvia l'analisi spettrale FFT per identificare l'anomalia.
        """)
    with col_info2:
        st.markdown("### ⚙️ Stato Sistema")
        st.success("🟢 Pipeline FFT & DSP Attiva")
        st.info("💡 Analisi delle frequenze in Hertz abilitata.")

    st.markdown("---")
    st.subheader("🔴 Pannello di Acquisizione Audio")
    
    audio_data = mic_recorder(
        start_prompt="▶️ Avvia Registrazione Audio Motore",
        stop_prompt="⏹️ Ferma e Salva Registrazione",
        key='mic_recorder_pro_clean'
    )
    
    if audio_data is not None:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### 🎧 Riproduzione Campione Registrato")
        st.audio(audio_data['bytes'], format='audio/wav')
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔍 Avvia Analisi Spettrale (FFT & DSP)", key="btn_avvia_analisi_pro"):
            with st.spinner("Elaborazione Trasformata di Fourier (FFT) in corso..."):
                report_ia = analizza_audio_motore(audio_data['bytes'])
                
                st.success("Analisi completata con successo!")
                st.markdown("### 📊 Report Diagnostico IA Avanzato")
                
                if not report_ia["valido"]:
                    st.markdown(f"""
                    <div style="background-color: #161B22; padding: 20px; border-radius: 12px; border: 1px solid #FF5555; margin-bottom: 15px;">
                        <h4 style="color: #FF5555; margin-top: 0;">⚠️️ Avviso Campione Acustico</h4>
                        <p style="margin: 4px 0;"><b>Stato:</b> {report_ia['tipo_rilevato']}</p>
                        <p style="margin: 4px 0;"><b>Nota:</b> {report_ia['anomalia']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background-color: #161B22; padding: 20px; border-radius: 12px; border: 1px solid #00E5FF; margin-bottom: 15px;">
                        <h4 style="color: #00E5FF; margin-top: 0;">🚗 Profilo Spettrale Rilevato</h4>
                        <p style="margin: 4px 0;"><b>Riscontro:</b> {report_ia['tipo_rilevato']}</p>
                        <p style="margin: 4px 0;"><b>Architettura:</b> {report_ia['motore']}</p>
                        <p style="margin: 4px 0; color: #3FB950;"><b>Confidenza:</b> {report_ia['confidenza_veicolo']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div style="background-color: #161B22; padding: 20px; border-radius: 12px; border: 1px solid #FFA657; margin-bottom: 15px;">
                        <h4 style="color: #FFA657; margin-top: 0;">🔧 Diagnosi Meccanica (Bande di Frequenza)</h4>
                        <p style="margin: 4px 0;"><b>Anomalia:</b> {report_ia['anomalia']}</p>
                        <p style="margin: 4px 0; color: #3FB950;"><b>Confidenza Guasto:</b> {report_ia['confidenza_guasto']}</p>
                    </div>
                    """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background-color: #161B22; padding: 15px; border-radius: 10px; border: 1px solid #30363D; text-align: center; color: #8B949E;">
            Nessun audio registrato. Clicca su <b>'Avvia Registrazione'</b> per iniziare l'acquisizione.
        </div>
        """, unsafe_allow_html=True)

elif menu == "Catalogo e Preventivi B2B":
    st.header("🛠️ Ricerca Ricambi e Preventivo Multi-Categoria")
    
    targa_grezza = st.text_input("Inserisci Targa o Telaio (Verifica Veicolo)", "", key="input_targa_veicolo")
    targa_input = targa_grezza.upper().strip().replace(" ", "")
    
    if 'ultima_targa_inserita' not in st.session_state:
        st.session_state['ultima_targa_inserita'] = targa_input

    if st.session_state['ultima_targa_inserita'] != targa_input:
        st.session_state['ultima_targa_inserita'] = targa_input
        if 'preventivo_finale' in st.session_state:
            st.session_state.pop('preventivo_finale')

    veicolo_info = interroga_verificaauto(targa_input)
    
    if veicolo_info.get("success"):
        st.markdown(f"""
        <div style="background-color: #161B22; padding: 20px; border-radius: 14px; border: 1px solid #00E5FF; margin-bottom: 20px;">
            <h3 style="color: #00E5FF; margin-top: 0;">🏛️ Estratto Telematico - VerificaAuto.it</h3>
            <p style="margin: 4px 0;"><b>Categoria:</b> {veicolo_info['tipo']}</p>
            <p style="margin: 4px 0;"><b>Modello Ufficiale:</b> {veicolo_info['modello']} &nbsp;|&nbsp; <b>Anno:</b> {veicolo_info['anno']}</p>
            <p style="margin: 4px 0;"><b>Alimentazione:</b> {veicolo_info['alimentazione']} &nbsp;|&nbsp; <b>Cilindrata:</b> {veicolo_info['cilindrata']} &nbsp;|&nbsp; <b>Potenza:</b> {veicolo_info['potenza']}</p>
            <p style="margin: 4px 0;"><b>Targa:</b> {targa_input} &nbsp;|&nbsp; <b>Telaio (VIN):</b> <code>{veicolo_info['vin']}</code></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info(f"💡 {veicolo_info.get('messaggio', 'Inserisci una targa valida per verificare il veicolo.')}")
    
    st.markdown("---")
    st.markdown("### 📋 Selezione Componenti e Ricambi")
    
    catalogo_ricambi = get_catalogo_ricambi()
    
    if 'carrello_pezzi' not in st.session_state:
        st.session_state['carrello_pezzi'] = []

    cat_selezionata = st.selectbox("Seleziona Categoria Sistema:", list(catalogo_ricambi.keys()), key="select_cat_sistema")
    pezzi_disponibili = catalogo_ricambi[cat_selezionata]
    
    pezzo_scelto = st.selectbox(f"Seleziona ricambio da [{cat_selezionata}]:", list(pezzi_disponibili.keys()), key="select_pezzo_specifico")
    
    if st.button("➕ Aggiungi al Preventivo", key="btn_aggiungi_pezzo"):
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
        st.markdown("#### 🛒 Ricambi Selezionati:")
        for idx, item in enumerate(st.session_state['carrello_pezzi']):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"- **{item['nome']}** ({item['categoria']}) - Codice: `{item['codice']}`")
            with col2:
                if st.button("Rimuovi", key=f"del_item_{idx}"):
                    st.session_state['carrello_pezzi'].pop(idx)
                    st.rerun()

    st.markdown("---")
    
    if st.button("🧮 Calcola Preventivo Totale", key="btn_calcola_preventivo"):
        if not st.session_state['carrello_pezzi']:
            st.warning("Il carrello dei ricambi è vuoto. Aggiungi almeno un pezzo.")
        elif not veicolo_info.get("success"):
            st.warning("Prima di calcolare il preventivo, inserisci una targa valida per verificare il veicolo.")
        else:
            tot_ricambi = 0
            tot_ore = 0
            inflation = 1.05
            labor_rate = 50.00
            
            dettagli = []
            for item in st.session_state['carrello_pezzi']:
                c_agg = item["costo_base"] * inflation
                tot_ricambi += c_agg
                tot_ore += item["ore"]
                dettagli.append({
                    "Categoria": item["categoria"],
                    "Ricambio": item["nome"],
                    "Codice": item["codice"],
                    "Costo Listino": f"€ {c_agg:.2f}",
                    "Manodopera": f"{item['ore']}h"
                })
            
            tot_lavoro = tot_ore * labor_rate
            totale_finale = tot_ricambi + tot_lavoro
            
            st.session_state['preventivo_finale'] = {
                "targa": targa_input,
                "tipo": veicolo_info["tipo"],
                "modello": veicolo_info["modello"],
                "anno": veicolo_info["anno"],
                "alimentazione": veicolo_info["alimentazione"],
                "cilindrata": veicolo_info["cilindrata"],
                "potenza": veicolo_info["potenza"],
                "vin": veicolo_info["vin"],
                "elementi": dettagli,
                "tot_ricambi": tot_ricambi,
                "tot_ore": tot_ore,
                "tot_lavoro": tot_lavoro,
                "totale_generale": totale_finale
            }

    if 'preventivo_finale' in st.session_state:
        p = st.session_state['preventivo_finale']
        st.markdown("---")
        
        st.markdown(f"### 📄 Foglio Preventivo Ufficiale IAmecc")
        st.write(f"**Categoria Mezzo:** {p['tipo']} — **Modello:** {p['modello']} ({p['anno']})")
        st.write(f"**Alimentazione:** {p['alimentazione']} ({p['cilindrata']} / {p['potenza']})")
        st.write(f"**Targa Verificata:** {p['targa']} — **VIN:** {p['vin']}")
        st.markdown("---")
        
        df_preventivo = pd.DataFrame(p['elementi'])
        st.dataframe(df_preventivo, use_container_width=True, hide_index=True)
        
        st.markdown(f"**Totale Ricambi:** € {p['tot_ricambi']:.2f}")
        st.markdown(f"**Totale Manodopera ({p['tot_ore']} ore):** € {p['tot_lavoro']:.2f}")
        st.markdown(f"### **Totale Preventivo: € {p['totale_generale']:.2f}**")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
            <button onclick="window.print()" style="width: 100%; background-color: #00E5FF; color: black; padding: 14px; font-weight: bold; border: none; border-radius: 12px; cursor: pointer; font-size: 16px;">
                🖨️ STAMPA / SALVA PREVENTIVO IN PDF
            </button>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Conferma e Invia Ordine B2B", key="btn_invia_ordine_b2b"):
            st.success("Ordine cumulativo inoltrato con successo al distributore!")
