# logic.py

import streamlit as st
import random
import os
from groq import Groq
from data import GAME_DATA, SUSPECT_IMAGES

# --- CONFIGURAZIONE CLIENT ---
@st.cache_resource(ttl="1h")
def get_groq_client():
    try:
        return Groq(api_key=st.secrets["GROQ_API_KEY"])
    except Exception as e:
        return None

client = get_groq_client()

# --- HELPER PERCORSI ---
current_dir = os.path.dirname(os.path.abspath(__file__))

def get_img_path(filename):
    return os.path.join(current_dir, "images", filename)

# --- INIZIALIZZAZIONE ---
def init_game():
    # Recupera lingua corrente (default IT se non settata)
    lang = st.session_state.get("language", "it")
    data = GAME_DATA[lang]

    st.session_state.solution = random.choice(data["scenarios"])
    st.session_state.game_started = False
    st.session_state.attempts = 0
    st.session_state.max_attempts = 15
    st.session_state.history_log = [] 
    st.session_state.game_over = False
    st.session_state.winner = False
    st.session_state.current_view = "hall" 
    st.session_state.input_key = 0
    st.session_state.show_gift = False
    st.session_state.suspect_stress = {}
    st.session_state.questions_per_suspect = {} 
    st.session_state.show_innocent_popup = False
    
    # Variabili anti-flash
    st.session_state.waiting_for_ai = False  
    st.session_state.pending_query = ""      

    # Alibi fissi (basati sulla lingua corrente)
    st.session_state.fixed_alibis = {}
    culprit = st.session_state.solution["culprit"]
    # Nota: le chiavi dei sospettati (nomi) sono uguali in entrambe le lingue
    all_suspects = list(data["personalities"].keys())
    
    for name in all_suspects:
        persona = data["personalities"][name]
        if name == culprit:
            selected_alibi = random.choice(persona["fake_alibi"])
        else:
            selected_alibi = random.choice(persona["innocent_alibi"])
        st.session_state.fixed_alibis[name] = selected_alibi

    # Testimone Chiave
    innocents = [s for s in all_suspects if s != culprit]
    st.session_state.key_witness = random.choice(innocents)

# --- AI RESPONSE LOGIC ---
def get_ai_response(suspect_name, question):
    if not client:
        return "Errore: API Key mancante."

    # Contesto e Lingua
    lang = st.session_state.get("language", "it")
    data = GAME_DATA[lang]
    ui_text = data["ui"]
    
    scenario = st.session_state.solution
    culprit = scenario["culprit"]
    key_witness = st.session_state.key_witness
    
    is_culprit = (suspect_name == culprit)
    is_key_witness = (suspect_name == key_witness)

    # Gestione Stress
    if suspect_name not in st.session_state.suspect_stress:
        st.session_state.suspect_stress[suspect_name] = 0
    st.session_state.suspect_stress[suspect_name] += 1 
    current_stress = st.session_state.suspect_stress[suspect_name]

    # Dati Statici Personaggio
    persona = data["personalities"][suspect_name]
    role_desc = data["suspects"][suspect_name]["role"]
    my_alibi = st.session_state.fixed_alibis.get(suspect_name, "...")
    
    # --- COSTRUZIONE SYSTEM PROMPT ---
    
    style_instruction = f"STYLE: {', '.join(persona['style'])}."
    
    # Fix per Rudolph (Reindeer behavior)
    if suspect_name == "Rudolph":
        style_instruction += "\nIMPORTANT: You are a reindeer. Do NOT speak fluently. Use sounds (snorts, jingles), actions between asterisks, and broken phrases."

    system_instruction = f"""
    {ui_text['system_intro']}
    Name: {suspect_name}
    Role: {role_desc}
    
    {style_instruction}
    Keep it short (max 2 sentences).

    CASE FACTS:
    - Evidence: "{scenario['evidence']}".
    """

    if is_culprit:
        system_instruction += f"""
        {ui_text['culprit_instr']}
        1. ALIBI: ALWAYS LIE. Say: "{my_alibi}".
        2. MOTIVE: Secret motive is "{scenario['motive']}". Hint at it only if angry.
        3. ACCUSATION: If accused, blame {random.choice(persona['blame'])}.
        Never repeat the exact same answer.
        """
    
    elif is_key_witness:
        system_instruction += f"""
        {ui_text['witness_instr']}
        Alibi: "{my_alibi}" (Truth).
        Never reveal the name of the real culprit.
        TRUST LEVEL (Current: {current_stress}/5):
        """
        if current_stress <= 2:
            system_instruction += f"- {ui_text['stress_low']}"
        elif current_stress <= 3:
            system_instruction += f"- {ui_text['stress_med']}'{scenario['trace_vague']}'"
        else:
            system_instruction += f"- {ui_text['stress_high']}'{scenario['trace_specific']}'"

    else: # Innocente inutile
        system_instruction += f"""
        {ui_text['innocent_instr']}
        Alibi: "{my_alibi}" (Truth).
        If asked who did it, guess wildly about {random.choice(persona['blame'])}.
        TRUST LEVEL (Current: {current_stress}/5):
        """
        if current_stress <= 2:
            system_instruction += f"- {ui_text['stress_low']}"
        else:
            system_instruction += f"- {ui_text['stress_med']}'{scenario['trace_vague']}'"

    # Chiamata API
    try:
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": f"Detective: {question}"}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.8,
            max_tokens=150,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return "(...Connection error...)"

# --- FUNZIONI INPUT / NAVIGAZIONE ---

def submit_question():
    if 'input_key' not in st.session_state:
        # Fallback se lo stato è perso
        st.session_state.language = "it"
        init_game()
        return

    key_name = f"input_{st.session_state.input_key}"
    if key_name in st.session_state:
        query = st.session_state[key_name]
        if not query: return

        if st.session_state.attempts >= st.session_state.max_attempts:
            st.session_state.game_over = True
            st.session_state.winner = False
            st.session_state.current_view = "hall"
            return 

        st.session_state.pending_query = query
        st.session_state.waiting_for_ai = True
        st.session_state.input_key += 1 

def process_ai_response():
    suspect = st.session_state.current_view
    query = st.session_state.pending_query
    
    ans = get_ai_response(suspect, query)
    
    st.session_state.history_log.append({"suspect": suspect, "q": query, "a": ans})
    st.session_state.attempts += 1
    
    if suspect not in st.session_state.questions_per_suspect:
        st.session_state.questions_per_suspect[suspect] = 0
    st.session_state.questions_per_suspect[suspect] += 1
    
    is_innocent = (suspect != st.session_state.solution["culprit"])
    if is_innocent and st.session_state.questions_per_suspect[suspect] == 5:
        st.session_state.show_innocent_popup = True
        
    st.session_state.waiting_for_ai = False

def start_game():
    st.session_state.game_started = True
    st.session_state.current_view = "hall"

def enter_room(suspect_name):
    st.session_state.current_view = suspect_name
    st.session_state.show_innocent_popup = False

def close_room():
    st.session_state.current_view = "hall"
    st.session_state.show_innocent_popup = False

def close_popup():
    st.session_state.show_innocent_popup = False

def make_accusation(suspect_name):
    culprit = st.session_state.solution["culprit"]
    if suspect_name == culprit:
        st.session_state.winner = True
    else:
        st.session_state.winner = False
    st.session_state.game_over = True