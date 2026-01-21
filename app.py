import streamlit as st

st.set_page_config(page_title="AlertAid", page_icon="🛑", layout="centered")

# ------------------- STYLING -------------------
st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF;
    }
    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 20px;
        color: #2E3A59;
        font-family: 'Arial', sans-serif;
    }
    .chatbox {
        max-width: 700px;
        margin: 0 auto;
        padding: 20px;
        border-radius: 20px;
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
    .input-area {
        position: fixed;
        bottom: 0;
        width: 100%;
        background: white;
        padding: 10px 0;
        box-shadow: 0 -1px 8px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------- TITLE -------------------
st.markdown('<div class="title">AlertAid</div>', unsafe_allow_html=True)

# ------------------- DISASTER FUNCTIONS -------------------
def earthquake_before():
    return "- Secure heavy furniture\n- Prepare emergency kit\n- Identify safe places in your home"

def earthquake_during():
    return "- Drop, Cover, and Hold On\n- Stay away from windows"

def earthquake_after():
    return "- Check for injuries\n- Be alert for aftershocks"

def earthquake_info():
    return "An earthquake is the sudden shaking of the ground caused by movements in the Earth's crust."

def typhoon_before():
    return "- Monitor weather updates\n- Secure loose objects\n- Prepare emergency supplies\n- Check evacuation routes"

def typhoon_during():
    return "- Stay indoors\n- Avoid floodwaters\n- Keep away from windows\n- Listen to official warnings"

def typhoon_after():
    return "- Avoid fallen power lines\n- Check for structural damage\n- Stay updated with official announcements"

def typhoon_info():
    return "A typhoon is a powerful tropical cyclone with strong winds and heavy rainfall."

def flood_before():
    return "- Prepare evacuation routes\n- Elevate appliances and important items\n- Store clean water and emergency supplies\n- Secure important documents"

def flood_during():
    return "- Move to higher ground immediately\n- Avoid walking or driving through floodwaters\n- Stay away from electrical wires\n- Listen to official alerts"

def flood_after():
    return "- Return home only when authorities say it’s safe\n- Clean and disinfect your home\n- Avoid contact with contaminated water\n- Check for damage"

def flood_info():
    return "A flood occurs when water overflows onto normally dry land."

def fire_before():
    return "- Check electrical wiring and outlets\n- Keep fire extinguishers ready\n- Install smoke detectors\n- Plan escape routes"

def fire_during():
    return "- Stay low to avoid smoke\n- Evacuate immediately\n- Use the nearest exit\n- Do not use elevators"

def fire_after():
    return "- Do not re-enter burned areas\n- Call emergency services if needed\n- Seek medical help for injuries\n- Contact authorities for safety inspection"

def fire_info():
    return "Fire is a rapid chemical reaction that produces heat, light, and smoke."

# ------------------- CHAT FUNCTION -------------------
def get_response(user_input):
    user_input = user_input.lower()

    # 🔥 FLOOD KEYWORDS
    if "what is" in user_input and "flood" in user_input:
        return flood_info()
    if "before" in user_input and "flood" in user_input:
        return flood_before()
    if "during" in user_input and "flood" in user_input:
        return flood_during()
    if "after" in user_input and "flood" in user_input:
        return flood_after()

    # 🔥 FIRE KEYWORDS
    if "what is" in user_input and "fire" in user_input:
        return fire_info()
    if "before" in user_input and "fire" in user_input:
        return fire_before()
    if "during" in user_input and "fire" in user_input:
        return fire_during()
    if "after" in user_input and "fire" in user_input:
        return fire_after()

    # 🔥 EARTHQUAKE KEYWORDS
    if "what is" in user_input and "earthquake" in user_input:
        return earthquake_info()
    if "before" in user_input and "earthquake" in user_input:
        return earthquake_before()
    if "during" in user_input and "earthquake" in user_input:
        return earthquake_during()
    if "after" in user_input and "earthquake" in user_input:
        return earthquake_after()

    # 🔥 TYPHOON KEYWORDS
    if "what is" in user_input and "typhoon" in user_input:
        return typhoon_info()
    if "before" in user_input and "typhoon" in user_input:
        return typhoon_before()
    if "during" in user_input and "typhoon" in user_input:
        return typhoon_during()
    if "after" in user_input and "typhoon" in user_input:
        return typhoon_after()

    return "Sorry, I didn't understand. Please ask a disaster-related question."

# ------------------- CHAT STATE -------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Hi! I’m AlertAid 🤖\nAsk me about flood, fire, earthquake, or typhoon."}
    ]

# ------------------- CHAT DISPLAY -------------------
st.markdown('<div class="chatbox">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user">{msg["text"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot">{msg["text"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ------------------- INPUT AREA (BOTTOM) -------------------
st.markdown('<div class="input-area">', unsafe_allow_html=True)

# --- INPUT ---
if "chat_input" not in st.session_state:
    st.session_state.chat_input = ""

col1, col2 = st.columns([4, 1])

with col1:
    st.text_input(" ", key="chat_input", placeholder="Type your message...", label_visibility="hidden")

with col2:
    if st.button("Send"):
        user_msg = st.session_state.chat_input.strip()
        if user_msg:
            st.session_state.messages.append({"role": "user", "text": user_msg})
            st.session_state.messages.append({"role": "bot", "text": get_response(user_msg)})

        st.session_state.chat_input = ""
