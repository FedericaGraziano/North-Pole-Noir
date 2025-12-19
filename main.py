# main.py
import streamlit as st
import os

from data import GAME_DATA, SUSPECT_IMAGES
from styles import load_css, create_snow_effect
import logic

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="North Pole Noir", page_icon="🎅", layout="wide")

# Carica stili
load_css()

# --- STATO INIZIALE & LINGUA ---
if 'language' not in st.session_state:
    st.session_state.language = None # Nessuna lingua selezionata all'inizio

if 'input_key' not in st.session_state:
    # Init parziale per evitare crash prima dello start
    st.session_state.game_started = False
    st.session_state.current_view = "landing"
    st.session_state.max_attempts = 0
    st.session_state.history_log = []

# ==========================================
# 1. LANDING PAGE (SELEZIONE LINGUA)
# ==========================================
if st.session_state.language is None:
    create_snow_effect()
    
    # Spaziatura per centrare visivamente
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # Titolo Ghiacciato
    st.markdown("""
        <div class='icy-title'>
            <h1>NORTH POLE NOIR</h1>
            <h3>A CHRISTMAS CRIME GAME</h3>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown("<div style='text-align: center; margin-bottom: 5px;'>Select Language / Seleziona Lingua</div>", unsafe_allow_html=True)
        
        # Menu a tendina
        lang_selection = st.selectbox(
            "Language", 
            options=["English", "Italiano"], 
            label_visibility="collapsed"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Pulsante Start
        if st.button("START GAME / INIZIA", use_container_width=True):
            # 1. Imposta lingua
            if lang_selection == "Italiano":
                st.session_state.language = "it"
            else:
                st.session_state.language = "en"
            
            # 2. Inizializza logica di gioco con la lingua corretta
            logic.init_game()
            
            # 3. Ricarica per andare alla view successiva
            st.rerun()

# ==========================================
# 2. FLUSSO DI GIOCO PRINCIPALE
# ==========================================
else:
    # Recupera i testi localizzati
    lang = st.session_state.language
    texts = GAME_DATA[lang]["ui"]
    suspects_data = GAME_DATA[lang]["suspects"]
    
    # --- SIDEBAR ---
    if st.session_state.game_started:
        with st.sidebar:
            st.markdown(f"### {texts['notebook']}")
            
            if st.session_state.max_attempts > 0:
                remaining = st.session_state.max_attempts - st.session_state.attempts
                st.write(f"**{texts['questions_left']}** {remaining}/{st.session_state.max_attempts}")
                st.progress(st.session_state.attempts / st.session_state.max_attempts)
            
            st.divider()

            if not st.session_state.history_log:
                st.markdown(f"*{texts['empty_notebook']}*")
            
            for log in reversed(st.session_state.history_log):
                st.markdown(f"""
                <div class="history-block">
                    <div class="history-char">🗣️ {log['suspect']}</div>
                    <div class="history-q">"{log['q']}"</div>
                    <div class="history-a">{log['a']}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.divider()
            if st.button(texts['reset_btn']):
                st.session_state.clear()
                # Torniamo alla selezione lingua
                st.session_state.language = None 
                st.rerun()

    # --- VIEW CONTROLLER ---

    # 2.1 INTRODUZIONE
    if not st.session_state.game_started:
        create_snow_effect()
        st.title(texts['title'])
        
        img_path = logic.get_img_path("All.png")
        if os.path.exists(img_path):
            intro_c1, intro_c2, intro_c3 = st.columns([1, 1.5, 1])
            with intro_c2:
                st.image(img_path, use_container_width=True)

        st.markdown(f"""
        ### {texts['subtitle']}
        <div style='font-size: 20px; font-family: "Courier New", monospace; line-height: 1.6; position: relative; z-index: 2;'>
        {texts['intro_text']}
        </div>
        <br>
        """, unsafe_allow_html=True)
        
        col_start1, col_start2, col_start3 = st.columns([1, 2, 1])
        with col_start2:
            st.markdown('<div class="start-btn">', unsafe_allow_html=True)
            st.button(texts['start_btn'], on_click=logic.start_game, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # 2.2 GIOCO FINITO (Vittoria/Sconfitta)
    elif st.session_state.game_over:
        st.markdown("<br><br>", unsafe_allow_html=True)
        scenario = st.session_state.solution
        
        win_video = "https://www.youtube.com/watch?v=DpwbyFltv6g&list=RDDpwbyFltv6g&start_radio=1"
        lose_video = "https://www.youtube.com/watch?v=ysIzPF3BfpQ"
        current_video = ""

        if st.session_state.winner:
            current_video = win_video
            st.balloons()
            st.markdown(f"""
                <div style="background-color: rgba(0, 255, 0, 0.1); padding: 30px; border-radius: 15px; border: 3px solid #00ff00; text-align: center;">
                    <h1 style="color: #00ff00;">{texts['win_title']}</h1>
                    <p style="font-size: 24px;">{texts['win_msg']} <b>{scenario['culprit']}</b>!</p>
                    <p><b>{texts['motive_label']}</b> {scenario['motive']}</p>
                    <p><b>{texts['evidence_label']}</b> {scenario['evidence']}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            current_video = lose_video
            st.markdown(f"""
                <div style="background-color: rgba(255, 75, 75, 0.1); padding: 30px; border-radius: 15px; border: 3px solid #ff4b4b; text-align: center;">
                    <h1 style="color: #ff4b4b;">{texts['lose_title']}</h1>
                    <p style="font-size: 24px;">{texts['lose_msg']} <b>{scenario['culprit']}</b>!</p>
                    <p><b>{texts['motive_label']}</b> {scenario['motive']}</p>
                    <p><b>{texts['evidence_label']}</b> {scenario['evidence']}</p>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        col_v1, col_v2, col_v3 = st.columns([1, 2, 1])
        with col_v2:
            if st.button(texts['gift_btn'], type="primary", use_container_width=True):
                 st.session_state.show_gift = True
            if st.session_state.show_gift:
                st.video(current_video)

        st.markdown('<br><div class="start-btn">', unsafe_allow_html=True)
        if st.button(texts['new_game_btn'], use_container_width=True):
            st.session_state.clear()
            st.session_state.language = lang # Mantiene la lingua scelta
            logic.init_game()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # 2.3 HALL CENTRALE
    elif st.session_state.current_view == "hall":
        st.markdown(f"### {texts['hall_title']}")
        
        # Nomi sospettati sono le chiavi (invariati tra lingue, es. Santa, Pip...)
        suspects_list = list(suspects_data.keys())
        col1, col2 = st.columns(2, gap="medium")
        
        def render_suspect_btn(name):
            # Usa SUSPECT_IMAGES per il nome file, suspects_data per i ruoli
            img_filename = SUSPECT_IMAGES[name]
            img_full_path = logic.get_img_path(img_filename)
            
            st.markdown('<div class="char-select-btn">', unsafe_allow_html=True)
            label = f"{texts['interrogate_btn']} {name}"
            st.button(label, key=f"btn_{name}", on_click=logic.enter_room, args=(name,), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            if os.path.exists(img_full_path):
                st.image(img_full_path, use_container_width=True)
            else:
                st.warning(f"Manca file: {img_filename}")

        with col1:
            render_suspect_btn(suspects_list[0])
            st.write("")
            render_suspect_btn(suspects_list[2])

        with col2:
            render_suspect_btn(suspects_list[1])
            st.write("")
            render_suspect_btn(suspects_list[3])

        st.divider()
        st.markdown(f"### {texts['accuse_section']}")
        cols = st.columns(4)
        for idx, s in enumerate(suspects_list):
            with cols[idx]:
                st.markdown('<div class="accusation-btn">', unsafe_allow_html=True)
                st.button(f"{texts['accuse_btn']} {s}", key=f"accuse_{s}", on_click=logic.make_accusation, args=(s,))
                st.markdown('</div>', unsafe_allow_html=True)

    # 2.4 STANZA INTERROGATORIO
    else:
        suspect = st.session_state.current_view
        domande_esaurite = st.session_state.attempts >= st.session_state.max_attempts

        # POPUP 1: SUGGERIMENTO INNOCENTE
        if st.session_state.show_innocent_popup and not domande_esaurite:
            st.markdown(f"""
            <div class="parchment-box">
                <h3>{texts['popup_innocent_title']}</h3>
                <p>{texts['popup_innocent_msg']}</p>
            </div>
            """, unsafe_allow_html=True)
            col_pop1, col_pop2, col_pop3 = st.columns([1,1,1])
            with col_pop2:
                 st.button(texts['popup_close'], on_click=logic.close_popup)
            st.divider()

        # POPUP 2: DOMANDE ESAURITE
        if domande_esaurite:
            st.markdown(f"""
            <div class="parchment-box" style="border: 4px solid #8b0000; background-color: #fceceb;">
                <h3 style="color: #8b0000 !important;">{texts['popup_end_title']}</h3>
                <p>{texts['popup_end_msg']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            col_end1, col_end2, col_end3 = st.columns([1, 2, 1])
            with col_end2:
                 st.button(texts['btn_go_accuse'], on_click=logic.close_room, type="primary", use_container_width=True)
            st.divider()

        # INTESTAZIONE STANZA
        head_c1, head_c2 = st.columns([5, 1])
        with head_c1:
            st.markdown(f"## {texts['room_title']} {suspect}")
        with head_c2:
            st.markdown('<div class="close-btn">', unsafe_allow_html=True)
            st.button(texts['back_hall'] if 'back_hall' in texts else "❌", on_click=logic.close_room)
            st.markdown('</div>', unsafe_allow_html=True)
    
        col_img, col_chat = st.columns([1, 2], gap="large")
        
        # FOTO E INFO
        with col_img:
            img_filename = SUSPECT_IMAGES[suspect]
            img_p = logic.get_img_path(img_filename)
            if os.path.exists(img_p):
                st.image(img_p, use_container_width=True)
            st.info(f"Ruolo: {suspects_data[suspect]['role']}")
        
        # CHAT E INPUT
        with col_chat:
            st.markdown(f"""
            <div style="background-color: #1c1f2b; border: 1px solid #4bddff; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                <h4 style="color: #4bddff; margin:0;">{texts['interrogation_box_title']}</h4>
                <p style="font-size: 16px;">{texts['interrogation_hint']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            last_exchange = next((x for x in reversed(st.session_state.history_log) if x['suspect'] == suspect), None)
            
            if last_exchange:
                st.chat_message("user").write(last_exchange['q'])
                with st.chat_message("assistant", avatar="🎅"):
                    st.write(last_exchange['a'])
            else:
                st.write(f"*{texts['no_questions_yet']}*")
            
            st.markdown("<br>", unsafe_allow_html=True) 
            
            # INPUT FIELD
            placeholder_text = f"{texts['placeholder']} {suspect}:"
            if domande_esaurite:
                placeholder_text = texts['placeholder_end']

            st.text_input(
                label=placeholder_text,
                key=f"input_{st.session_state.input_key}", 
                on_change=logic.submit_question, 
                disabled=domande_esaurite or st.session_state.waiting_for_ai
            )

            # SPINNER
            if st.session_state.get('waiting_for_ai', False):
                with st.spinner(f"🎅 {suspect} {texts['spinner']}"):
                    logic.process_ai_response()
                st.rerun()