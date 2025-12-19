# styles.py
import streamlit as st
import random

def load_css():
    st.markdown("""
    <style>
        .stApp { background-color: #0e1117; color: #ffffff; }
        
        /* Font base Desktop */
        .stMarkdown p, .stText p, .stHtml p { font-size: 19px !important; color: #ffffff !important; line-height: 1.6; }
        h1, h2, h3 { position: relative; z-index: 2; color: #ffffff !important; }
        
        /* Input Fields */
        .stTextInput label { font-size: 22px !important; color: #4bddff !important; font-weight: bold; margin-bottom: 10px; }
        .stTextInput input { font-size: 20px !important; color: #ffffff !important; background-color: #1c1f2b !important; border: 1px solid #4c4c4c; border-radius: 8px; }
        .stTextInput input:focus { border-color: #4bddff !important; box-shadow: 0 0 5px rgba(75, 221, 255, 0.5); }
        
        /* Bottoni Generici */
        .stButton > button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; font-size: 18px !important; background-color: #262730; color: #ffffff !important; border: 2px solid #4c4c4c; transition: all 0.3s ease; }
        .stButton > button:hover { background-color: #363945; border-color: #4bddff; box-shadow: 0 0 10px rgba(75, 221, 255, 0.3); color: #ffffff !important; }
        
        /* Bottone Start */
        .start-btn button { background-color: #4bddff !important; color: #0e1117 !important; font-size: 26px !important; height: 4em; border: none !important; box-shadow: 0 0 15px rgba(75, 221, 255, 0.4); }
        .start-btn button:hover { background-color: #ffffff !important; color: #0e1117 !important; box-shadow: 0 0 20px rgba(255, 255, 255, 0.6); }
        
        /* Bottoni Accusa */
        .accusation-btn > button { background-color: transparent !important; border: 3px solid #ff4b4b !important; color: #ff4b4b !important; font-size: 18px !important; height: 3.5em; }
        .accusation-btn > button:hover { background-color: #ff4b4b !important; color: #ffffff !important; box-shadow: 0 0 15px rgba(255, 75, 75, 0.6); }

        /* Bottoni Selezione Personaggio */
        .char-select-btn > button { 
            background-color: #1c1f2b !important; 
            border-radius: 15px !important; 
            border: 2px solid #4bddff !important; 
            color: #4bddff !important; 
            font-size: 20px !important; 
            text-transform: uppercase; 
            letter-spacing: 1px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.5), 0 0 5px rgba(75, 221, 255, 0.2); 
            transition: transform 0.2s; 
            margin-bottom: 5px;
            height: auto !important;
            padding: 10px !important;
        }
        .char-select-btn > button:hover { 
            transform: translateY(-3px); 
            box-shadow: 0 8px 20px rgba(0,0,0,0.6), 0 0 10px rgba(75, 221, 255, 0.4); 
            background-color: #1c1f2b !important;
            color: #ffffff !important;
        }

        /* Sidebar History */
        section[data-testid="stSidebar"] { background-color: #151820; border-right: 1px solid #262730; }
        .history-block { background-color: #1c1f2b; border-left: 3px solid #4bddff; padding: 10px; margin-bottom: 10px; border-radius: 5px; }
        .history-char { font-weight: bold; color: #4bddff; font-size: 14px; text-transform: uppercase; margin-bottom: 5px; }
        .history-q { font-style: italic; color: #cccccc; font-size: 14px; }
        .history-a { color: #ffffff; font-size: 15px; margin-top: 5px; }

        /* Close Button */
        .close-btn button { background-color: transparent !important; border: 1px solid #4c4c4c !important; color: #aaa !important; width: 50px !important; }
        .close-btn button:hover { color: #fff !important; border-color: #fff !important; }

        /* POPUP PERGAMENA */
        .parchment-box {
            background-color: #f4e4bc;
            border: 4px solid #8b5a2b;
            color: #4a3b2a !important;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.7);
            font-family: 'Courier New', monospace;
        }
        .parchment-box h3 { color: #8b5a2b !important; font-weight: bold; margin-bottom: 10px; }
        .parchment-box p { color: #4a3b2a !important; font-weight: bold; font-size: 18px !important; }

        /* TITOLO GHIACCIATO (NEW) */
        .icy-title {
            text-align: center;
            margin-bottom: 30px;
        }
        .icy-title h1 {
            font-family: 'Arial Black', sans-serif;
            font-size: 70px !important;
            background: -webkit-linear-gradient(#ffffff, #a3d9ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0px 0px 15px rgba(75, 221, 255, 0.8), 0px 0px 30px rgba(0, 115, 230, 0.6);
            margin-bottom: 0;
        }
        .icy-title h3 {
             color: #4bddff !important;
             font-family: 'Courier New', monospace;
             letter-spacing: 3px;
             text-shadow: 0px 0px 10px rgba(75, 221, 255, 0.5);
             margin-top: -10px;
        }

        /* --- MOBILE OPTIMIZATION --- */
        @media only screen and (max-width: 600px) {
            .stMarkdown p, .stText p, .stHtml p { font-size: 16px !important; }
            h1 { font-size: 26px !important; }
            h2 { font-size: 22px !important; }
            h3 { font-size: 20px !important; }
            .start-btn button { font-size: 20px !important; height: 3.5em; }
            .char-select-btn > button { font-size: 16px !important; }
            .accusation-btn > button { font-size: 16px !important; }
            .stTextInput input { font-size: 16px !important; }
            .stTextInput label { font-size: 18px !important; }
            .parchment-box { padding: 10px; }
            .parchment-box p { font-size: 16px !important; }
            .icy-title h1 { font-size: 40px !important; }
        }
    </style>
    """, unsafe_allow_html=True)

def create_snow_effect():
    num_flakes = 100
    html_snow = '<div class="snow-container">'
    css_snow = """
    <style>
        .snow-container {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: 99999; pointer-events: none; overflow: hidden;
        }
        .snowflake {
            position: absolute; top: -10px; background: white; border-radius: 50%; opacity: 0.8;
        }
        @keyframes snowfall {
            0% { transform: translate(0, -10px); opacity: 1; }
            100% { transform: translate(calc(20px + 50px * var(--random-sway)), 105vh); opacity: 0; }
        }
    """
    for i in range(num_flakes):
        left_pos = random.uniform(0, 100)
        size = random.uniform(4, 10)
        duration = random.uniform(3, 8)
        delay = random.uniform(0, 5)
        sway_seed = random.uniform(-1, 1)
        css_snow += f"""
        .flake-{i} {{
            left: {left_pos}vw; width: {size}px; height: {size}px;
            --random-sway: {sway_seed};
            animation: snowfall {duration}s linear {delay}s infinite;
        }}
        """
        html_snow += f'<div class="snowflake flake-{i}"></div>'
    css_snow += "</style>"
    html_snow += "</div>"
    st.markdown(css_snow + html_snow, unsafe_allow_html=True)