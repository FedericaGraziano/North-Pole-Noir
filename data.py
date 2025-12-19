# data.py

SUSPECT_IMAGES = {
    "Mrs. Claus": "Ms_Santa.jpg",
    "Pip": "Pip.jpg",
    "Rudolph": "Rudolph.png",
    "Santa": "Santa.png"
}

GAME_DATA = {
    "it": {
        "ui": {
            "title": "North Pole Noir",
            "subtitle": "Il sacco scomparso",
            "start_btn": "🎅 INIZIA LE INDAGINI 🎅",
            "notebook": "📝 Taccuino del Detective",
            "questions_left": "Domande Rimaste:",
            "empty_notebook": "Il taccuino è vuoto. Inizia a interrogare!",
            "reset_btn": "🔄 Reset Totale Gioco",
            "hall_title": "📍 Hall Centrale: Scegli chi interrogare",
            "interrogate_btn": "INTERROGA",
            "accuse_section": "⚖️ Accusa Finale",
            "accuse_btn": "Accusa",
            "room_title": "Stanza di",
            "interrogation_box_title": "Interrogatorio in corso...",
            "interrogation_hint": "Chiedi del suo alibi ('Dov'eri?'), chi sospetta o cosa ha visto.",
            "placeholder": "Fai una domanda a",
            "placeholder_end": "⛔ DOMANDE ESAURITE. PROCEDI ALL'ACCUSA.",
            "spinner": "sta riflettendo sulla tua domanda...",
            "no_questions_yet": "(Nessuna domanda fatta ancora a questo sospettato)",
            "popup_innocent_title": "📜 Lista dei 'Buoni'",
            "popup_innocent_msg": "Questo sospettato sembra fin troppo tranquillo. Forse è meglio interrogare qualcun altro?",
            "popup_close": "Ho capito, cambio stanza",
            "popup_end_title": "🎅 La Lista dei Cattivi 📜",
            "popup_end_msg": "STOP! Hai esaurito le domande (15/15). Devi accusare ora!",
            "btn_go_accuse": "VADO AD ACCUSARE! ⚖️",
            "win_title": "🎉 CASO RISOLTO! 🎉",
            "win_msg": "Il colpevole è",
            "lose_title": "🕸️ Colpevole sbagliato! 🕸️",
            "lose_msg": "Era stato",
            "motive_label": "Movente:",
            "evidence_label": "Prova:",
            "gift_btn": "🎁 Al mio regalo",
            "new_game_btn": "🔄 Nuova Indagine",
            "intro_text": """
        Sono le <b>19:00 della vigilia di Natale</b>. 
        Qualcuno ha rubato il Grande Sacco dei Giocattoli!
        <br><br>
        <div style="text-align: center; color: #4bddff; font-size: 24px; font-weight: bold;">
        Il colpevole è uno di loro... forse anche lo stesso Babbo Natale?
        </div>
        <br>
        Interroga i sospettati, cerca il movente e trova il colpevole prima di mezzanotte.
        Sei pronto Detective?
            """,
            # System Prompts
            "system_intro": "Sei un personaggio di un giallo natalizio. Parla ITALIANO.",
            "culprit_instr": "RUOLO: SEI IL COLPEVOLE. MENTI sul tuo alibi. Se menzionano la prova, vai nel panico.",
            "innocent_instr": "RUOLO: SEI INNOCENTE. Dì la verità sul tuo alibi. Non sai nulla.",
            "witness_instr": "RUOLO: SEI UN TESTIMONE INNOCENTE (ma agitato). Dì la verità sul tuo alibi.",
            "stress_low": "Sei diffidente. Dì che non hai visto nulla di importante.",
            "stress_med": "Inizi a fidarti. Rivela un indizio vago con tono misterioso: ",
            "stress_high": "Ti fidi completamente! RIVELA L'INDIZIO CHIAVE: "
        },
        "suspects": {
            "Mrs. Claus": { "role": "La moglie" },
            "Pip": { "role": "Elfo Scriba" },
            "Rudolph": { "role": "Renna Leader" },
            "Santa": { "role": "Il Capo" }
        },
        "scenarios": [
            {
                "culprit": "Santa", 
                "motive": "Burnout natalizio e la moglie vuole metterlo a dieta.",
                "evidence": "Lista calorie bruciacchiata e briciole di 'Biscotto triplo zenzero'.",
                "trace_specific": "C'erano briciole di biscotti allo zenzero e un foglio...una lista forse.", 
                "trace_vague": "Ho visto qualcosa di sbriciolato a terra, forse segatura?"
            },
            {
                "culprit": "Rudolph", 
                "motive": "Invidia delle altre renne perchè le altre ricevono più carote e lavorano meno.", 
                "evidence": "Carota morsicata 'Carota Gran Reserve'.",
                "trace_specific": "Ho trovato un pelo ispido. Non sembra di elfo. E qualcos'altro a terra...ma non erano biscotti", 
                "trace_vague": "C'era un odore dolce...diverso dal solito odore natalizio"
            },
            {
                "culprit": "Mrs. Claus", 
                "motive": "Vuole mettere tutti a dieta perché è stufa di cucinare sempre per tutti.", 
                "evidence": "Lista calorie: 'Dieta senza biscotti!'.",
                "trace_specific": "Si sentiva un forte profumo di cannella e biscotti...molto natalizio.", 
                "trace_vague": "C'era un profumo dolce nell'aria, quasi piacevole."
            },
            {
                "culprit": "Pip", 
                "motive": "Vuole automatizzare il Natale é stufo di scrivere liste a mano.", 
                "evidence": "Progetto 'Sacco 4.0' per automatizzare il Natale con l'AI.",
                "trace_specific": "C'erano macchie fresche di inchiostro e una lista di nomi.", 
                "trace_vague": "Ho visto delle macchie scure sul muro, sembrava sporco."
            }
        ],
        "personalities": {
            "Santa": {
                "style": ["Ho-ho... ehm...", "Figliolo, dimmi.", "Sono occupato con la lista...", "Per le corna di una renna!"],
                "fake_alibi": ["Ero a contare le stelle!", "Dormivo profondamente.", "Lucidavo la slitta.", "Preparavo biscotti"],
                "innocent_alibi": ["Ero nel mio studio.", "Mangiavo biscotti.", "Controllavo il meteo.", "Preparavo il piano di viaggio"],
                "blame": ["Pip è troppo ambizioso.", "Forse mia moglie?", "Chiederei alle renne"]
            },
            "Mrs. Claus": {
                "style": ["Tesoro caro...", "I biscotti bruciano, sbrigati.", "Ho una casa da gestire.", "Sbrighiamoci...fa freddo fuori."],
                "fake_alibi": ["Passeggiavo nella bufera.", "Ero in cantina da sola.", "Davo fieno alle renne.", "Lucidavo la slitta"],
                "innocent_alibi": ["Rammendavo i calzini.", "Preparavo il cacao per i biscotti.", "Facevo l'inventario.", "Preparavo i biscotti per il viaggio di mio marito"],
                "blame": ["Mio marito è stanco.", "Pip trama qualcosa.", "Quelle renne non mi convincono"]
            },
            "Pip": {
                "style": ["Non ho fatto niente!", "Ho il modulo 4B da finire!", "Sono solo un umile elfo.", "Niente accuse senza prove!"],
                "fake_alibi": ["Ero nell'archivio segreto.", "Aiutavo Santa...perché lui dormiva come sempre", "Facevo l'inventario dei glitter.", "Controllavo che il vestito di Santa fosse al suo posto"],
                "innocent_alibi": ["Ero al reparto reclami.", "Temperavo matite.", "Aggiornavo il server.", "Ricontrollavo le liste di buoni e cattivi"],
                "blame": ["Santa ha le chiavi.", "Rudolph vuole comandare.", "La moglie di Santa è stufa della negligenza del marito"]
            },
            "Rudolph": {
                "style": ["*Sbuffo luminoso*", "*Scalpita*", "*Ti fissa masticando*", "*Agita il campanello*"],
                "fake_alibi": ["Volavo sopra le nuvole.", "Ero nel bosco.", "Ero con Santa...a mangiare carote"],
                "innocent_alibi": ["Lucidavo le corna.", "Dormivo sulla paglia.", "Facevo stretching.", "Motivavo le altre renne prima del viaggio"],
                "blame": ["*Indica Santa*", "*Sbuffa verso Pip*", "*Guarda storto Mrs. Claus*"]
            }
        }
    },
    
    "en": {
        "ui": {
            "title": "North Pole Noir",
            "subtitle": "The Missing Sack",
            "start_btn": "🎅 START INVESTIGATION 🎅",
            "notebook": "📝 Detective's Notebook",
            "questions_left": "Questions Left:",
            "empty_notebook": "The notebook is empty. Start interrogating!",
            "reset_btn": "🔄 Reset Game",
            "hall_title": "📍 Main Hall: Choose who to interrogate",
            "interrogate_btn": "INTERROGATE",
            "accuse_section": "⚖️ Final Accusation",
            "accuse_btn": "Accuse",
            "room_title": "Room of",
            "interrogation_box_title": "Interrogation in progress...",
            "interrogation_hint": "Ask about their alibi ('Where were you?'), who they suspect, or what they saw.",
            "placeholder": "Ask a question to",
            "placeholder_end": "⛔ NO QUESTIONS LEFT. ACCUSE NOW.",
            "spinner": "is thinking about your question...",
            "no_questions_yet": "(No questions asked yet)",
            "popup_innocent_title": "📜 The 'Good List'",
            "popup_innocent_msg": "This suspect seems too calm. Maybe check someone else?",
            "popup_close": "Got it, leaving room",
            "popup_end_title": "🎅 The Naughty List 📜",
            "popup_end_msg": "STOP! You used all your questions (15/15). You must accuse now!",
            "btn_go_accuse": "I'M READY TO ACCUSE! ⚖️",
            "win_title": "🎉 CASE SOLVED! 🎉",
            "win_msg": "The culprit is",
            "lose_title": "🕸️ Wrong Suspect! 🕸️",
            "lose_msg": "It was actually",
            "motive_label": "Motive:",
            "evidence_label": "Evidence:",
            "gift_btn": "🎁 Get my gift",
            "new_game_btn": "🔄 New Investigation",
            "intro_text": """
        It is <b>7:00 PM on Christmas Eve</b>. 
        Someone has stolen the Big Sack of Toys!
        <br><br>
        <div style="text-align: center; color: #4bddff; font-size: 24px; font-weight: bold;">
        The culprit is one of them... maybe even Santa himself?
        </div>
        <br>
        Interrogate the suspects, find the motive, and catch the culprit before midnight.
        Are you ready, Detective?
            """,
            # System Prompts
            "system_intro": "You are a character in a Christmas murder mystery. Speak ENGLISH.",
            "culprit_instr": "ROLE: YOU ARE THE CULPRIT. LIE about your alibi. If evidence is mentioned, panic.",
            "innocent_instr": "ROLE: YOU ARE INNOCENT. Tell the truth about your alibi. You know nothing.",
            "witness_instr": "ROLE: YOU ARE AN INNOCENT WITNESS (but nervous). Tell the truth about your alibi.",
            "stress_low": "You are suspicious. Say you saw nothing important.",
            "stress_med": "You start trusting. Reveal a vague clue mysteriously: ",
            "stress_high": "You trust completely! REVEAL THE KEY CLUE: "
        },
        "suspects": {
            "Mrs. Claus": { "role": "The Wife" },
            "Pip": { "role": "Scribe Elf" },
            "Rudolph": { "role": "Lead Reindeer" },
            "Santa": { "role": "The Boss" }
        },
        "scenarios": [
            {
                "culprit": "Santa", 
                "motive": "Christmas burnout and his wife put him on a diet.",
                "evidence": "Burnt calorie list and ginger cookie crumbs.",
                "trace_specific": "There were ginger cookie crumbs and a list...", 
                "trace_vague": "I saw something crumbled on the floor, maybe sawdust?"
            },
            {
                "culprit": "Rudolph", 
                "motive": "Jealousy of other reindeer getting more carrots.", 
                "evidence": "Bitten 'Grand Reserve' carrot.",
                "trace_specific": "I found a stiff hair. Not an elf's. And something else on the ground...", 
                "trace_vague": "There was a sweet smell... different from the usual Christmas scents."
            },
            {
                "culprit": "Mrs. Claus", 
                "motive": "She wants to put everyone on a diet, tired of cooking.", 
                "evidence": "Calorie list: 'No Cookie Diet!'.",
                "trace_specific": "There was a strong smell of cinnamon and cookies... very festive.", 
                "trace_vague": "There was a sweet scent in the air, almost pleasant."
            },
            {
                "culprit": "Pip", 
                "motive": "Wants to automate Christmas, tired of handwriting lists.", 
                "evidence": "Project 'Sack 4.0' to automate Christmas with AI.",
                "trace_specific": "There were fresh ink stains and a list of names.", 
                "trace_vague": "I saw dark stains on the wall, looked like dirt."
            }
        ],
        "personalities": {
            "Santa": {
                "style": ["Ho-ho... um...", "My child, tell me.", "I'm busy with the list...", "By my reindeer's antlers!"],
                "fake_alibi": ["I was counting stars!", "I was sleeping deeply.", "Polishing the sleigh.", "Baking cookies"],
                "innocent_alibi": ["I was in my study.", "Eating cookies.", "Checking the weather.", "Planning the trip"],
                "blame": ["Pip is too ambitious.", "Maybe my wife?", "Ask the reindeer"]
            },
            "Mrs. Claus": {
                "style": ["Oh dear...", "The cookies are burning, hurry.", "I have a house to run.", "Let's hurry... it's cold outside."],
                "fake_alibi": ["Walking in the blizzard.", "I was in the cellar alone.", "Feeding the reindeer.", "Polishing the sleigh"],
                "innocent_alibi": ["Darning socks.", "Making cocoa.", "Doing inventory.", "Packing cookies for my husband"],
                "blame": ["My husband is tired.", "Pip is plotting something.", "Those reindeer look suspicious"]
            },
            "Pip": {
                "style": ["I did nothing!", "I have form 4B to finish!", "I'm just a humble elf.", "No accusations without proof!"],
                "fake_alibi": ["I was in the secret archive.", "Helping Santa... because he was sleeping", "Counting glitter.", "Checking Santa's suit"],
                "innocent_alibi": ["I was at the complaints dept.", "Sharpening pencils.", "Updating the server.", "Checking the nice list"],
                "blame": ["Santa has the keys.", "Rudolph wants to lead.", "Santa's wife is tired of his negligence"]
            },
            "Rudolph": {
                "style": ["*Glowing snort*", "*Stomps*", "*Stares while chewing*", "*Jingles bells*"],
                "fake_alibi": ["Flying above clouds.", "In the woods.", "With Santa... eating carrots"],
                "innocent_alibi": ["Polishing antlers.", "Sleeping on straw.", "Stretching.", "Motivating the team"],
                "blame": ["*Points at Santa*", "*Snorts at Pip*", "*Glares at Mrs. Claus*"]
            }
        }
    }
}