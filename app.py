import streamlit as st

st.set_page_config(page_title="AlertAid", page_icon="🛑")

# ------------------- STYLING -------------------
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        margin-bottom: 50px;
        color: #2E3A59;
        font-family: 'Arial', sans-serif;
    }
    .user {
        text-align: right;
        background-color: #DCF8C6;
        padding: 12px;
        border-radius: 20px;
        width: fit-content;
        max-width: 70%;
        float: right;
        clear: both;
        margin: 5px 0;
    }
    .bot {
        text-align: left;
        background-color: #F1F0F0;
        padding: 12px;
        border-radius: 20px;
        width: fit-content;
        max-width: 70%;
        float: left;
        clear: both;
        margin: 5px 0;
    }
    .container {
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------- TITLE -------------------
st.markdown('<div class="title">AlertAid</div>', unsafe_allow_html=True)

# ------------------- DISASTER FUNCTIONS -------------------
def earthquake_before():
    return "🌍 EARTHQUAKE – BEFORE\n- Secure heavy furniture\n- Prepare emergency kit\n- Identify safe places in your home"

def earthquake_during():
    return "🌍 EARTHQUAKE – DURING\n- Drop, Cover, and Hold On\n- Stay away from windows"

def earthquake_after():
    return "🌍 EARTHQUAKE – AFTER\n- Check for injuries\n- Be alert for aftershocks"

def earthquake_info():
    return "🌍 WHAT IS AN EARTHQUAKE?\nAn earthquake is the sudden shaking of the ground caused by movements in the Earth's crust."

def typhoon_before():
    return "🌪️ TYPHOON – BEFORE\n- Monitor weather updates\n- Secure loose objects"

def typhoon_during():
    return "🌪️ TYPHOON – DURING\n- Stay indoors\n- Avoid floodwaters"

def typhoon_after():
    return "🌪️ TYPHOON – AFTER\n- Avoid fallen power lines"

def typhoon_info():
    return "🌪️ WHAT IS A TYPHOON?\nA typhoon is a powerful tropical cyclone with strong winds and heavy rainfall."

def flood_before():
    return "🌊 FLOOD – BEFORE\n- Prepare evacuation routes\n- Elevate appliances"

def flood_during():
    return "🌊 FLOOD – DURING\n- Move to higher ground\n- Do not walk through floodwaters"

def flood_after():
    return "🌊 FLOOD – AFTER\n- Clean and disinfect your home"

def flood_info():
    return "🌊 WHAT IS A FLOOD?\nA flood occurs when water overflows onto normally dry land."

def fire_before():
    return "🔥 FIRE – BEFORE\n- Check electrical wiring\n- Keep fire extinguishers ready"

def fire_during():
    return "🔥 FIRE – DURING\n- Stay low to avoid smoke\n- Evacuate immediately"

def fire_after():
    return "🔥 FIRE – AFTER\n- Do not re-enter burned areas"

def fire_info():
    return "🔥 WHAT IS A FIRE?\nFire is a rapid chemical reaction that produces heat, light, and smoke."

# ------------------- CHAT FUNCTION -------------------
def get_response(user_input):
    user_input = user_input.lower()

    if "what is" in user_input and "earthquake" in user_input:
        return earthquake_info()
    elif "what is" in user_input and "typhoon" in user_input:
        return typhoon_info()
    elif "what is" in user_input and "flood" in user_input:
        return flood_info()
    elif "what is" in user_input and "fire" in user_input:
        return fire_info()

    elif "earthquake" in user_input:
        if "before" in user_input:
            return earthquake_before()
        elif "during" in user_input:
            return earthquake_during()
        elif "after" in user_input:
            return earthquake_after()

    elif "typhoon" in user_input:
        if "before" in user_input:
            return typhoon_before()
        elif "during" in user_input:
            return typhoon_during()
        elif "after" in user_input:
            return typhoon_after()

    elif "flood" in user_input:
        if "before" in user_input:
            return flood_before()
        elif "during" in user_input:
            return flood_during()
        elif "after" in user_input:
            return flood_after()

    elif "fire" in user_input:
        if "before" in user_input:
            return fire_before()
        elif "during" in user_input:
            return fire_during()
        elif "after" in user_input:
            return fire_after()

    else:
        return "Sorry, I didn't understand."

# ------------------- CHAT STATE -------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.form(key="chat_form"):
    user_input = st.text_input("", key="user_input_text")
    submit = st.form_submit_button("Send")

    if submit and user_input:
        st.session_state.messages.append({"role": "user", "text": user_input})
        bot_response = get_response(user_input)
        st.session_state.messages.append({"role": "bot", "text": bot_response})

# ------------------- DISPLAY CHAT -------------------
st.markdown('<div class="container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user">{msg["text"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot">{msg["text"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
        text-align: left;
        background-color: #F1F0F0;
        padding: 10px;
        border-radius: 15px;
        margin: 5px 0;
        width: fit-content;
        float: left;
        clear: both;
    }
    .chatbox {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>AlertAid</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Disaster Information Chatbot</div>", unsafe_allow_html=True)

# ------------------- DISASTER INFO FUNCTIONS -------------------
def earthquake_before():
    return "🌍 EARTHQUAKE – BEFORE\n- Secure heavy furniture\n- Prepare emergency kit\n- Identify safe places in your home"

def earthquake_during():
    return "🌍 EARTHQUAKE – DURING\n- Drop, Cover, and Hold On\n- Stay away from windows"

def earthquake_after():
    return "🌍 EARTHQUAKE – AFTER\n- Check for injuries\n- Be alert for aftershocks"

def earthquake_info():
    return "🌍 WHAT IS AN EARTHQUAKE?\nAn earthquake is the sudden shaking of the ground caused by movements in the Earth's crust."

def typhoon_before():
    return "🌪️ TYPHOON – BEFORE\n- Monitor weather updates\n- Secure loose objects"

def typhoon_during():
    return "🌪️ TYPHOON – DURING\n- Stay indoors\n- Avoid floodwaters"

def typhoon_after():
    return "🌪️ TYPHOON – AFTER\n- Avoid fallen power lines"

def typhoon_info():
    return "🌪️ WHAT IS A TYPHOON?\nA typhoon is a powerful tropical cyclone with strong winds and heavy rainfall."

def flood_before():
    return "🌊 FLOOD – BEFORE\n- Prepare evacuation routes\n- Elevate appliances"

def flood_during():
    return "🌊 FLOOD – DURING\n- Move to higher ground\n- Do not walk through floodwaters"

def flood_after():
    return "🌊 FLOOD – AFTER\n- Clean and disinfect your home"

def flood_info():
    return "🌊 WHAT IS A FLOOD?\nA flood occurs when water overflows onto normally dry land."

def fire_before():
    return "🔥 FIRE – BEFORE\n- Check electrical wiring\n- Keep fire extinguishers ready"

def fire_during():
    return "🔥 FIRE – DURING\n- Stay low to avoid smoke\n- Evacuate immediately"

def fire_after():
    return "🔥 FIRE – AFTER\n- Do not re-enter burned areas"

def fire_info():
    return "🔥 WHAT IS A FIRE?\nFire is a rapid chemical reaction that produces heat, light, and smoke."

# ------------------- CHAT FUNCTION -------------------
def get_response(user_input):
    user_input = user_input.lower()

    if "what is" in user_input and "earthquake" in user_input:
        return earthquake_info()
    elif "what is" in user_input and "typhoon" in user_input:
        return typhoon_info()
    elif "what is" in user_input and "flood" in user_input:
        return flood_info()
    elif "what is" in user_input and "fire" in user_input:
        return fire_info()

    elif "earthquake" in user_input:
        if "before" in user_input:
            return earthquake_before()
        elif "during" in user_input:
            return earthquake_during()
        elif "after" in user_input:
    return "🌊 FLOOD – AFTER\n- Clean and disinfect your home"

def flood_info():
    return "🌊 WHAT IS A FLOOD?\nA flood occurs when water overflows onto normally dry land."

def fire_before():
    return "🔥 FIRE – BEFORE\n- Check electrical wiring\n- Keep fire extinguishers ready"

def fire_during():
    return "🔥 FIRE – DURING\n- Stay low to avoid smoke\n- Evacuate immediately"

def fire_after():
    return "🔥 FIRE – AFTER\n- Do not re-enter burned areas"

def fire_info():
    return "🔥 WHAT IS A FIRE?\nFire is a rapid chemical reaction that produces heat, light, and smoke."

# ------------------- CHAT FUNCTION -------------------
def get_response(user_input):
    user_input = user_input.lower()

    if "what is" in user_input and "earthquake" in user_input:
        return earthquake_info()
    elif "what is" in user_input and "typhoon" in user_input:
        return typhoon_info()
    elif "what is" in user_input and "flood" in user_input:
        return flood_info()
    elif "what is" in user_input and "fire" in user_input:
        return fire_info()

    elif "earthquake" in user_input:
        if "before" in user_input:
            return earthquake_before()
        elif "during" in user_input:
            return earthquake_during()
        elif "after" in user_input:
            return earthquake_after()

    elif "typhoon" in user_input:
        if "before" in user_input:
            return typhoon_before()
        elif "during" in user_input:
            return typhoon_during()
        elif "after" in user_input:
            return typhoon_after()

    elif "flood" in user_input:
        if "before" in user_input:
            return flood_before()
        elif "during" in user_input:
            return flood_during()
        elif "after" in user_input:
            return flood_after()

    elif "fire" in user_input:
        if "before" in user_input:
            return fire_before()
        elif "during" in user_input:
            return fire_during()
        elif "after" in user_input:
            return fire_after()

    else:
        return "Sorry, I didn't understand. Please ask about a disaster and mention before/during/after or what is <disaster>."

# ------------------- STREAMLIT CHAT UI -------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("", key="input")

if st.button("Send"):
    if user_input:
        st.session_state.messages.append({"role": "user", "text": user_input})
        bot_response = get_response(user_input)
        st.session_state.messages.append({"role": "bot", "text": bot_response})
        st.session_state.input = ""

# Display chat messages only
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style="
                text-align: right;
                background-color: #DCF8C6;
                padding: 10px;
                border-radius: 15px;
                margin: 5px 0;
                width: fit-content;
                float: right;
                clear: both;">
                {msg['text']}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="
                text-align: left;
                background-color: #F1F0F0;
                padding: 10px;
                border-radius: 15px;
                margin: 5px 0;
                width: fit-content;
                float: left;
                clear: both;">
                {msg['text']}
            </div>
            """,
            unsafe_allow_html=True
        )

def flood_after():
    return "🌊 FLOOD – AFTER\n- Clean and disinfect your home"

def flood_info():
    return "🌊 WHAT IS A FLOOD?\nA flood occurs when water overflows onto normally dry land."

def fire_before():
    return "🔥 FIRE – BEFORE\n- Check electrical wiring\n- Keep fire extinguishers ready"

def fire_during():
    return "🔥 FIRE – DURING\n- Stay low to avoid smoke\n- Evacuate immediately"

def fire_after():
    return "🔥 FIRE – AFTER\n- Do not re-enter burned areas"

def fire_info():
    return "🔥 WHAT IS A FIRE?\nFire is a rapid chemical reaction that produces heat, light, and smoke."

# ------------------- CHAT FUNCTION -------------------
def get_response(user_input):
    user_input = user_input.lower()

    if "what is" in user_input and "earthquake" in user_input:
        return earthquake_info()
    elif "what is" in user_input and "typhoon" in user_input:
        return typhoon_info()
    elif "what is" in user_input and "flood" in user_input:
        return flood_info()
    elif "what is" in user_input and "fire" in user_input:
        return fire_info()

    elif "earthquake" in user_input:
        if "before" in user_input:
            return earthquake_before()
        elif "during" in user_input:
            return earthquake_during()
        elif "after" in user_input:
            return earthquake_after()

    elif "typhoon" in user_input:
        if "before" in user_input:
            return typhoon_before()
        elif "during" in user_input:
            return typhoon_during()
        elif "after" in user_input:
            return typhoon_after()

    elif "flood" in user_input:
        if "before" in user_input:
            return flood_before()
        elif "during" in user_input:
            return flood_during()
        elif "after" in user_input:
            return flood_after()

    elif "fire" in user_input:
        if "before" in user_input:
            return fire_before()
        elif "during" in user_input:
            return fire_during()
        elif "after" in user_input:
            return fire_after()

    else:
        return "Sorry, I didn't understand. Please ask about a disaster and mention before/during/after or what is <disaster>."

# ------------------- STREAMLIT CHAT UI -------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", key="input")

if st.button("Send"):
    if user_input:
        st.session_state.messages.append({"role": "user", "text": user_input})
        bot_response = get_response(user_input)
        st.session_state.messages.append({"role": "bot", "text": bot_response})
        st.session_state.input = ""

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div style='text-align: right; background-color:#DCF8C6; padding:10px; border-radius:10px; margin:5px 0'>{msg['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; background-color:#F1F0F0; padding:10px; border-radius:10px; margin:5px 0'>{msg['text']}</div>", unsafe_allow_html=True)
# -------- TYPHOON --------
def typhoon_before():
    return """
🌪️ TYPHOON – BEFORE
- Monitor weather updates
- Secure loose objects
"""

def typhoon_during():
    return """
🌪️ TYPHOON – DURING
- Stay indoors
- Avoid floodwaters
"""

def typhoon_after():
    return """
🌪️ TYPHOON – AFTER
- Avoid fallen power lines
"""

def typhoon_info():
    return """
🌪️ WHAT IS A TYPHOON?
A typhoon is a powerful tropical cyclone with strong winds and heavy rainfall.
"""

# -------- FLOOD --------
def flood_before():
    return """
🌊 FLOOD – BEFORE
- Prepare evacuation routes
- Elevate appliances
"""

def flood_during():
    return """
🌊 FLOOD – DURING
- Move to higher ground
- Do not walk through floodwaters
"""

def flood_after():
    return """
🌊 FLOOD – AFTER
- Clean and disinfect your home
"""

def flood_info():
    return """
🌊 WHAT IS A FLOOD?
A flood occurs when water overflows onto normally dry land.
"""

# -------- FIRE --------
def fire_before():
    return """
🔥 FIRE – BEFORE
- Check electrical wiring
- Keep fire extinguishers ready
"""

def fire_during():
    return """
🔥 FIRE – DURING
- Stay low to avoid smoke
- Evacuate immediately
"""

def fire_after():
    return """
🔥 FIRE – AFTER
- Do not re-enter burned areas
"""

def fire_info():
    return """
🔥 WHAT IS A FIRE?
Fire is a rapid chemical reaction that produces heat, light, and smoke.
"""

# -------- CHAT FUNCTION --------
def get_response(user_input):
    user_input = user_input.lower()

    # INFORMATION
    if "what is" in user_input and "earthquake" in user_input:
        return earthquake_info()
    elif "what is" in user_input and "typhoon" in user_input:
        return typhoon_info()
    elif "what is" in user_input and "flood" in user_input:
        return flood_info()
    elif "what is" in user_input and "fire" in user_input:
        return fire_info()

    # EARTHQUAKE ACTIONS
    elif "earthquake" in user_input:
        if "before" in user_input:
            return earthquake_before()
        elif "during" in user_input:
            return earthquake_during()
        elif "after" in user_input:
            return earthquake_after()

    # TYPHOON ACTIONS
    elif "typhoon" in user_input:
        if "before" in user_input:
            return typhoon_before()
        elif "during" in user_input:
            return typhoon_during()
        elif "after" in user_input:
            return typhoon_after()

    # FLOOD ACTIONS
    elif "flood" in user_input:
        if "before" in user_input:
            return flood_before()
        elif "during" in user_input:
            return flood_during()
        elif "after" in user_input:
            return flood_after()

    # FIRE ACTIONS
    elif "fire" in user_input:
        if "before" in user_input:
            return fire_before()
        elif "during" in user_input:
            return fire_during()
        elif "after" in user_input:
            return fire_after()

    else:
        return "Please ask using 'before', 'during', 'after', or 'what is <disaster>'."

# -------- STREAMLIT UI --------
user_input = st.text_input("Ask your question here:")

if st.button("Send"):
    response = get_response(user_input)
    st.write(response)
